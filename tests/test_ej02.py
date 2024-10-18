import pytest
from src.ej02_def import recibe_horasycoste

@pytest.mark.parametrize("horas, coste, expected", [

    (10, 10, 100),
    (12, 24, 288),
    (5, 4, 20)

])
def test_recibe_horasycoste(horas, coste, expected):
    assert recibe_horasycoste(horas, coste) == expected
