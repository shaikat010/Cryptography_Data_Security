import requests
import time

API_URL = "https://api-inference.huggingface.co/models/Apisate/DialoGPT-small-jordan"
headers = {"Authorization": "Bearer {Token_ID}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


output = query({
    # "inputs": {
    # 	"past_user_inputs": ["Which movie is the best ?"],
    # 	"generated_responses": ["It's Die Hard for sure."],
    # 	"text": "Can you explain why ?"
    # }

    "inputs": {
        "text": input()
    },
})

time.sleep(2)
print(output)

