from fastapi import FastAPI, HTTPException
from src.recargas import procesar_recarga, MontoInvalidoError

app = FastAPI(title="RecargaYa API REST")


@app.get("/calcular-recarga")
def calcular_recarga(monto: int, plan: str = "estandar"):
    try:
        bono_porcentaje = procesar_recarga(monto, plan)
        datos_bono = (monto * bono_porcentaje) // 100
        total_datos = monto + datos_bono
        return {
            "mensaje": "Recarga calculada exitosamente",
            "monto_ingresado": monto,
            "tipo_plan": plan,
            "bono_aplicado_porcentaje": bono_porcentaje,
            "total_datos_megas": total_datos
        }
    except MontoInvalidoError as e:

        raise HTTPException(status_code=400, detail=str(e))