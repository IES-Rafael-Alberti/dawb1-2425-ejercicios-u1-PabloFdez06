import pytest
from src.prueba1 import retornar_numero

@pytest.mark.parametrize("num1, num2, expected", [

    (0, 0, 0),
    (4, 4, 0),
    (5, 8, 8)

])
def test_retornar_numero(num1, num2, expected):
    assert retornar_numero(num1, num2) == expected
