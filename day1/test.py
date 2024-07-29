import requests

qna_list = [
    ("대한민국 건국 시기는 언제인가요?", "역사 선생님"),
    ("한글을 만든 조선시대의 왕은 누구인가요?", "역사 선생님"),
    ("세계에서 가장 높은 산은?", "지리 선생님"),
    ("세계에서 가장 큰 도시는 어디인가요?", "지리 선생님"),
    ("세계에서 가장 긴 강은 무엇인가요?", "지리 선생님"),
    ("세계에서 가장 큰 바다는 무엇인가요?", "지리 선생님"),
    ("세계에서 가장 큰 호수는 무엇인가요?", "지리 선생님"),
    ("세계에서 가장 큰 섬은 무엇인가요?", "지리 선생님"),
]


prompt_fname = "prompt4"
with open(f'./day1/prompt/{prompt_fname}.txt', 'r') as file:
    prompt = file.read().strip()

url = "http://localhost:11434/api/generate"

for q, a in qna_list:
    response = requests.post(url, json={
        "model": "llama3",
        "prompt": f"{prompt} \n{q}",
        "stream": False
    })

    print(f"Q: {q}")
    print(f"A: {response.json()['response']}")
    print(f"Expected: {a}")
    print()