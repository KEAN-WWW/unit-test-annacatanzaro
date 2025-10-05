"""Testing division function from calculator"""
import pytest
from app.calculator import Calculator

def test_division():
    """Divides two numbers"""
    result = Calculator.division(4, 1)
    assert result == 4, "Returns value"

def test_divided_by_zero():
    """Divides by zero"""
    with pytest.raises(ZeroDivisionError):
        Calculator.division(2, 0)
