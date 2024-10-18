import pytest
from src.ej11_def import recibe_num

@pytest.mark.parametrize("num, expected", [

    (10, 55.0),
    (25, 325.0),
    (100, 5050.0)

])
def test_recibe_num(num, expected):
    assert recibe_num(num) == expected
