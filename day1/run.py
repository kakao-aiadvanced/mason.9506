import requests

url = "http://localhost:11434/api/generate"

response = requests.post(url, json={
    "model": "llama3",
    "prompt": "대한민국의 수도는 어디인가요?",
    "stream": False
})

print(response.json()['response'])