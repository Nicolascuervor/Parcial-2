from fastapi.testclient import TestClient
from src.api import app

client = TestClient(app)

def test_endpoint_recarga_valida():

    respuesta = client.get("/calcular-recarga?monto=30000&plan=premium")
    assert respuesta.status_code == 200
    assert respuesta.json()["bono_aplicado_porcentaje"] == 30

def test_endpoint_recarga_invalida():
    respuesta = client.get("/calcular-recarga?monto=500")
    assert respuesta.status_code == 400
    assert "monto de recarga" in respuesta.json()["detail"]