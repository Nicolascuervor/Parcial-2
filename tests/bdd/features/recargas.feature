Feature: Módulo de Recargas de Celular RecargaYa S.A.S.
  Como usuario de RecargaYa
  Quiero recargar el saldo de mi celular
  Para obtener datos de navegación y bonificaciones según mi monto y plan

  Scenario: Rechazar recarga por monto inferior al límite
    Given que un cliente intenta recargar 999 pesos
    When el sistema valida el monto
    Then la recarga debe ser rechazada por monto inválido

  Scenario: Rechazar recarga por monto superior al límite
    Given que un cliente intenta recargar 50001 pesos
    When el sistema valida el monto
    Then la recarga debe ser rechazada por exceder el tope máximo

  Scenario Outline: Calcular bonificaciones según monto y tipo de plan
    Given que un cliente con plan "<tipo_plan>" solicita recargar <monto> pesos
    When el sistema procesa la recarga exitosamente
    Then el porcentaje de bonificacion aplicado debe ser del <bono_porcentaje> por ciento

    Examples:
      | tipo_plan | monto | bono_porcentaje | Notas / Razón de la prueba                    |
      | estandar  | 1000  | 0               | Límite mínimo válido, sin bono                |
      | estandar  | 9999  | 0               | Límite justo antes del primer bono            |
      | estandar  | 10000 | 10              | Límite exacto del bono del 10%                |
      | premium   | 10000 | 15              | Límite exacto del bono del 10% + 5% premium   |
      | estandar  | 29999 | 10              | Límite justo antes del bono máximo            |
      | estandar  | 30000 | 25              | Límite exacto del bono del 25%                |
      | premium   | 30000 | 30              | Límite exacto del bono del 25% + 5% premium   |
      | estandar  | 50000 | 25              | Límite máximo válido                          |
      | premium   | 1000  | 5               | Recarga baja, pero con 5% de bono por premium |