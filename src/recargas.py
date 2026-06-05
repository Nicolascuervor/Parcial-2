class MontoInvalidoError(Exception):
    pass

def procesar_recarga(monto: int, tipo_plan: str) -> int:

    if monto < 1000 or monto > 50000:
        raise MontoInvalidoError("El monto de recarga debe estar entre $1.000 y $50.000")

    bono = 0
    if monto >= 30000:
        bono = 25
    elif monto >= 10000:
        bono = 10

    if tipo_plan.lower() == "premium":
        bono += 5
        
    return bono