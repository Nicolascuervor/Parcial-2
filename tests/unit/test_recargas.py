import pytest
from src.recargas import procesar_recarga, MontoInvalidoError


def test_monto_inferior_rechazado():
    with pytest.raises(MontoInvalidoError):
        procesar_recarga(999, "estandar")
def test_monto_superior_rechazado():
    with pytest.raises(MontoInvalidoError):
        procesar_recarga(50001, "estandar")

@pytest.mark.parametrize("monto, tipo_plan, bono_esperado", [
    (1000, "estandar", 0),
    (9999, "estandar", 0),
    (10000, "estandar", 10),
    (10000, "premium", 15),
    (29999, "estandar", 10),
    (30000, "estandar", 25),
    (30000, "premium", 30),
    (50000, "estandar", 25),
    (1000, "premium", 5),
])
def test_calcular_bonificaciones(monto, tipo_plan, bono_esperado):
    porcentaje_obtenido = procesar_recarga(monto, tipo_plan)
    assert porcentaje_obtenido == bono_esperado