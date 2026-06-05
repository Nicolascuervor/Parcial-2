import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from src.recargas import procesar_recarga, MontoInvalidoError

scenarios('features/recargas.feature')

@pytest.fixture
def contexto():
    return {}

@given(parsers.parse('que un cliente intenta recargar {monto} pesos'))
def cliente_recarga_invalida(contexto, monto):
    contexto["monto"] = int(monto)
    contexto["plan"] = "estandar"

@given(parsers.parse('que un cliente con plan "{tipo_plan}" solicita recargar {monto} pesos'))
def cliente_recarga_valida(contexto, tipo_plan, monto):
    contexto["monto"] = int(monto)
    contexto["plan"] = tipo_plan

@when('el sistema valida el monto')
@when('el sistema procesa la recarga exitosamente')
def procesar(contexto):
    try:
        contexto["bono_obtenido"] = procesar_recarga(contexto["monto"], contexto["plan"])
    except MontoInvalidoError:
        contexto["hubo_error"] = True

@then('la recarga debe ser rechazada por monto inválido')
@then('la recarga debe ser rechazada por exceder el tope máximo')
def verificar_rechazo(contexto):
    assert contexto.get("hubo_error") is True

@then(parsers.parse('el porcentaje de bonificacion aplicado debe ser del {bono_esperado} por ciento'))
def verificar_bono(contexto, bono_esperado):
    assert contexto["bono_obtenido"] == int(bono_esperado)