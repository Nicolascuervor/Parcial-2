# Módulo de Recargas - RecargaYa S.A.S.

Este proyecto implementa el backend de facturación de recargas móviles aplicando metodologías ágiles: TDD, BDD, y automatización en CI/CD.

## Reglas de Negocio Implementadas
- Rango de recarga válido: $1.000 a $50.000.
- Montos >= $10.000 reciben un 10% de bonificación en datos.
- Montos >= $30.000 reciben un 25% de bonificación en datos.
- Usuarios con plan "premium" obtienen un 5% adicional acumulable.

## Instrucciones de Ejecución Local

Para ejecutar este proyecto necesitas tener `uv` instalado.

### 1. Pruebas Unitarias y de Comportamiento (TDD/BDD)
Ejecuta la validación de todos los escenarios Gherkin y los valores límite usando Pytest:
```bash
uv run pytest tests/