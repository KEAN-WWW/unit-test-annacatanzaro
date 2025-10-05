"""Testing addition function from calculator"""
from app.calculator import Calculator

def test_addition():
    """Adds two numbers"""
    result = Calculator.addition(3, 4)
    assert result == 7, "Returns value"
