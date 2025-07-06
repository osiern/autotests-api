import httpx
from tools.fakers import get_random_email  # Импортируем функцию для генерации случайного email

# Создаем пользователя
create_user_payload = {
    "email": get_random_email(),  # Используем функцию для генерации случайного email
    "password": "string",
    "lastName": "Petrov",
    "firstName": "Petr",
    "middleName": "Petrovich"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()

print("Status Code:", create_user_response.status_code)
print('Create user data:', create_user_response_data)

# Проходим аутентификацию
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Status Code:", login_response.status_code)
print('Login data:', login_response_data)

# Изменяем ранее созданного пользователя
patch_user_payload = {
    "email": get_random_email(),  # Используем функцию для генерации случайного email
    "password": "string",
    "lastName": "Kozulkin",
    "firstName": "Nos",
    "middleName": "Petrovich"
}

patch_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
patch_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=patch_user_headers,
    json=patch_user_payload
)
patch_user_response_data = patch_user_response.json()

print("Status Code:", patch_user_response.status_code)
print('Patch user data:', patch_user_response_data)


