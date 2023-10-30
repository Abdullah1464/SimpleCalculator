from app import square, sub, div, multiply

#Tests
def test_square():
    assert "4" == square(2)
def test_sub():
    assert "1" == sub(4)
def test_div():
    assert "2" == div(4,2)
def test_multiply():
    assert "4" == multiply(2,2)
    
