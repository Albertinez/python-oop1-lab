from lib.coffee import Coffee

def test_tip():
    c = Coffee("Medium", 5)
    c.tip()  # Should print message
    assert c.price == 6
