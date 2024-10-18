import pytest
from src.ej01_def import recibe_nombre

@pytest.mark.parametrize("nombre, expected", [

    ("pablo", "pablo"),
    ("patata", "patata"),
    ("hola", "hola")

])
def test_recibe_nombre(nombre, expected):
    assert recibe_nombre(nombre) == expected
