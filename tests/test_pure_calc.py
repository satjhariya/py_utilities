from pyUtils.src.pure_calc import pure_calc

def test_add():
    c = pure_calc()
    assert c.add(5,3) == 8
    assert c.add(10,3) == 13
    assert c.add(2,3) == 5

def test_subtract():
    c = pure_calc()
    assert c.subtract(5,3) == 2
    assert c.subtract(10,3) == 7
    assert c.subtract(2,3) == -1

def test_multiply():
    c = pure_calc()
    assert c.multiply(5,3) == 15
    assert c.multiply(10,3) == 30
    assert c.multiply(2,3) == 6

def test_divide():  
    c = pure_calc()
    assert c.divide(6,3) == 2
    assert c.divide(10,2) == 5
    assert c.divide(9,3) == 3
    try:
        c.divide(4,0)
        assert False, "Expected ValueError for division by zero"
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed"
