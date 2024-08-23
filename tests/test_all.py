from myFile import add, subtract, divide, multiply

def test_add():
    assert add(4,1) == 5

def test_subtract():
    assert subtract(4,1) == 3

def test_multiply():
    assert multiply(4,1) == 4

def test_divide():
    assert divide(4,1) == 0

