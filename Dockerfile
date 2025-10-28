# Використовуємо офіційний базовий образ Python 3.10
FROM python:3.10-slim

# Встановлюємо робочу директорію в контейнері
WORKDIR /app

# Копіюємо файл залежностей
COPY requirements.txt .

# !!! --- НОВИЙ БЛОК --- !!!
# Встановлюємо C-бібліотеки, необхідні для mysqlclient
# (pkg-config, gcc, та mysql development headers)
RUN apt-get update && apt-get install -y pkg-config default-libmysqlclient-dev build-essential && rm -rf /var/lib/apt/lists/*
# !!! --- КІНЕЦЬ НОВОГО БЛОКУ --- !!!

# Тепер встановлюємо Python-залежності
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо решту коду застосунку
COPY . .

# Визначаємо змінну оточення, щоб Flask знав, який файл запускати
ENV FLASK_APP=app.py

# Визначаємо порт
EXPOSE 8000

# Команда для запуску
CMD ["gunicorn", "--chdir", "/app", "--bind", "0.0.0.0:8000", "app:app"]
