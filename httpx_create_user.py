import httpx
from tools.fakers import get_random_email  # Импортируем функцию для генерации случайного email

payload = {
    "email": get_random_email(),  # Используем функцию для генерации случайного email
    "password": "string",
    "lastName": "Kozulkin",
    "firstName": "Nos",
    "middleName": "Petrovich"
}
response = httpx.post("http://localhost:8000/api/v1/users", json=payload)

print(response.status_code)
print(response.json())