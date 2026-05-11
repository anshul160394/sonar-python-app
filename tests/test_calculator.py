import pytest
from app.calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(2, 3) == 5
    assert calc.add(-1, 1) == 0
    assert calc.add(0, 0) == 0

def test_subtract(calc):
    assert calc.subtract(10, 4) == 6
    assert calc.subtract(0, 5) == -5
    assert calc.subtract(-3, -3) == 0

def test_multiply(calc):
    assert calc.multiply(3, 4) == 12
    assert calc.multiply(-2, 5) == -10
    assert calc.multiply(0, 100) == 0

def test_divide(calc):
    assert calc.divide(10, 2) == 5.0
    assert calc.divide(7, 2) == 3.5
    assert calc.divide(-6, 3) == -2.0

def test_divide_by_zero(calc):
    with pytest.raises(ValueError, match="Cannot divide by zero."):
        calc.divide(5, 0)

def test_power(calc):
    assert calc.power(2, 3) == 8
    assert calc.power(5, 0) == 1
    assert calc.power(3, 2) == 9

def test_modulus(calc):
    assert calc.modulus(10, 3) == 1
    assert calc.modulus(20, 5) == 0

def test_modulus_zero(calc):
    with pytest.raises(ValueError, match="Cannot perform modulus with zero."):
        calc.modulus(10, 0)
