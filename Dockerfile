FROM python:3.12-alpine

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем зависимости
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем исходники
COPY ./app .

# Команда запуска (замени на свою entrypoint-точку)
CMD ["python"]