from locust import HttpUser, task, between, events
import random


class ClienteRecargas(HttpUser):

    wait_time = between(1, 2)

    @task
    def realizar_recargas(self):

        monto_random = random.randint(1000, 50000)
        plan = random.choice(["estandar", "premium"])

        self.client.get(f"/calcular-recarga?monto={monto_random}&plan={plan}")

@events.quitting.add_listener
def verificar_rendimiento_p95(environment, **kwargs):
    if environment.stats.total.num_requests == 0:
        return

    p95 = environment.stats.total.get_response_time_percentile(0.95)
    print(f"\n--- RESULTADOS DEL ESTRÉS ---")
    print(f"Tiempo de respuesta P95: {p95} ms")

    if p95 > 300:
        print("FALLO: El tiempo P95 supera el límite estricto de 300ms.")
        environment.process_exit_code = 1
    else:
        print("ÉXITO: El sistema cumple con la métrica de rendimiento (P95 < 300ms).")