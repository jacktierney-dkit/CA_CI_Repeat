import pytest
import invoice as inv

def test_load_stock(tmp_stock_file):
    got = inv.loadStock(str(tmp_stock_file))
    assert got == [["pencil", 0.15, 85], ["folder", 1.4, 40]]

def test_items(stock):
    assert inv.itemList(stock)[0].startswith("1 : pencil")
    assert inv.getItemName(stock, 1) == "folder"
    assert inv.getItemNumber(stock, "folder") == 1
    assert inv.getPrice(stock, 0) == pytest.approx(0.15)
    assert inv.availableQuantity(stock, 1) == 40

@pytest.mark.parametrize("amount,code", [(10, "EUR"), (10, "USD"), (10, "GBP")])
def test_rates(amount, code):
    want = round(amount * inv.RATES[code], 2)
    assert inv.getCurrencyValue(amount, code) == want

def test_vat_and_discount():
    assert inv.calculateVAT(100) == pytest.approx(22.0)
    assert inv.discount(19.99) == 0.0
    assert inv.discount(20.01) == pytest.approx(round(20.01 * 0.10, 2))
    assert inv.discount(50.01) == pytest.approx(round(50.01 * 0.20, 2))

def test_make_invoice(stock):
    before = stock[0][2]
    price, total, disc, vat, net = inv.createInvoiceData(stock, 0, 10, "EUR")
    assert (price, total, disc, vat, net) == pytest.approx((0.15, 1.50, 0.00, 0.33, 1.83))
    assert stock[0][2] == before - 10

def test_orders_file(tmp_orders_file):
    row = ["eraser", 3, "EUR", 0.6, 1.8, 0.0, 0.4, 2.2]
    ok = inv.saveOrderToFile(str(tmp_orders_file), row)
    assert ok == 0
    first = open(tmp_orders_file).read().splitlines()[0]
    assert first == ",".join(map(str, row))

def test_stock_save_load(stock, tmp_path):
    out = tmp_path / "stock_out.txt"
    inv.saveStockData(str(out), stock)
    again = inv.loadStock(str(out))
    assert again == stock
