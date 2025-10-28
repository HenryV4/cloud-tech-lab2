from locust import HttpUser, task, between
class MyRestUser(HttpUser):
    wait_time = between(1, 3) # Даємо йому час
    host = "https://hotel-api-lab2-851473349647.europe-west3.run.app"
    @task
    def get_root(self):
        self.client.get("/")
