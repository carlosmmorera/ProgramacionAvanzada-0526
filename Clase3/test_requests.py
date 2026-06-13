import requests

url = "http://127.0.0.1:8000/users/"

user_data = {
    "username": "jnjna"*10,
    "email": "juan@example.com",
    "age": 51
}

response = requests.post(url, json=user_data)
print(f"Código de respuesta: {response.status_code}")
print(f"Respuesta: {response.json()}")

response = requests.get("http://localhost:8000/hello/carlos")
print(response.status_code)
print(response.json())