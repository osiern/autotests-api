import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "sborpisemiznet@gmail.com",
    "password": "qwerty"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Полученные токены:", login_response_data)
print("Status Code:", login_response.status_code)

# Получаем accessToken из вложенного словаря
access_token = login_response_data.get("token", {}).get("accessToken")

# Заголовок с токеном
headers = {"Authorization": f"Bearer {access_token}"}

# GET-запрос к /users/me
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
user_response_data = user_response.json()

print("Данные пользователя:", user_response_data)
print("Status Code:", user_response.status_code)