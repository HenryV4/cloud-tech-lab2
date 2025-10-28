from locust import HttpUser, task, between

class MyRestUser(HttpUser):
    # Тепер затримка може бути меншою, 
    # оскільки сам запит "важкий"
    wait_time = between(0.5, 1) 
    host = "https://hotel-api-lab2-851473349647.europe-west3.run.app"

    @task
    def load_cpu_endpoint(self):
        """ Створюємо РЕАЛЬНЕ навантаження на CPU """
        self.client.get("/cpu_load")

    # @task(1)
    # def get_root(self): ... (видаляємо старі завдання)
