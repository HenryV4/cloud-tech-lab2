from locust import HttpUser, task, between

class MyRestUser(HttpUser):
    # Імітуємо затримку між запитами від 1 до 3 секунд
    wait_time = between(1, 3)

    # ВАЖЛИВО: Вставте сюди URL вашого Cloud Run сервісу
    host = "https://hotel-api-lab2-851473349647.europe-west3.run.app"

    @task(1) # Це завдання виконується рідше
    def get_root(self):
        """ Завдання 1: Емулятор генерації запитів до веб сайту (головна сторінка) """
        self.client.get("/")

    @task(3) # Це завдання виконується в 3 рази частіше
    def get_locations(self):
        """ Завдання 2: Навантаження на REST сервіс (отримання локацій) """
        # Припускаємо, що у вас є ендпоінт /api/location (якщо ні, замініть на той, що є)
        # Нам потрібен ендпоінт, який робить запит до БАЗИ ДАНИХ, 
        # щоб створити реальне навантаження.
        self.client.get("/api/locations")
