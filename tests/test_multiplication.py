"""Testing multiplication function from calculator"""
from app.calculator import Calculator

def test_multiplication():
    """Multiplies two numbers"""
    result = Calculator.multiplication(2, 2)
    assert result == 4, "Returns value"
