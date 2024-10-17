import pytest
from src.ej04_def2 import convertir_a_fahrenheit

@pytest.mark.parametrize("input_celsius, expected", [

    (0, 32),
    (-4, 24.8),
    (50, 122)

])
def test_convertir_a_fahrenheit(input_celsius, expected):
    assert convertir_a_fahrenheit(input_celsius) == expected
