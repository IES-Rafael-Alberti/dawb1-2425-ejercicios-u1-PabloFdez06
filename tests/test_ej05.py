import pytest
from src.ej05_def2 import precio_iva

@pytest.mark.parametrize("porcentaje, importe, expected", [

    (115, 1500, 1815.00),
    (120, 1000, 1210.00),
    (40, 1000, 1400.00)

])
def test_precio_iva(porcentaje, importe, expected):
    assert precio_iva(porcentaje, importe) == expected
