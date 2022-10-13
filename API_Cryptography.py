import requests

API_URL = "https://api-inference.huggingface.co/models/xlm-roberta-base"
headers = {"Authorization": f"Bearer {Token_ID}"}


def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()


#The user should be giving a unique response phrase to generate the key words

output = query({
    "inputs": "The answer to the universe is <mask> and nothing.",
})


print(output)

#print(output)

passwords_keys = []

for i in output:
  #print(i)
  for j in i:
    if(j == 'sequence'):
      print(i[j])
      x = i[j]
      x = x.split(" ")
      passwords_keys.append(x[-3])

print(passwords_keys)


def key_generator():
    pass




