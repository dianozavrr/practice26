import requests
import json

get_url = "https://catfact.ninja/fact"
get_response = requests.get(get_url)
print("=== GET СТАТУС ===", get_response.status_code)
try:
    data_json = get_response.json()
    print("Факт про котика:", data_json["fact"])
except json.JSONDecodeError:
    print(get_response.text)

post_url = "https://httpbin.org/post"
post_data = {
    "example": "Це тестовий POST",
    "description": "Тест для перевірки"
}
post_response = requests.post(post_url, json=post_data)
print("\n=== POST СТАТУС ===", post_response.status_code)
try:
    post_json = post_response.json()
    print("Дані, які відправили в POST:", post_json["json"])
except json.JSONDecodeError:
    print(post_response.text)
