"""Testing subtraction function from calculator"""
from app.calculator import Calculator

def test_subtraction():
    """Subtracts two numbers"""
    result = Calculator.subtraction(2, 2)
    assert result == 0, "Returns value"
