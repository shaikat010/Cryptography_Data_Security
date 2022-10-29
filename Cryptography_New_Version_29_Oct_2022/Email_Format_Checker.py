

# Email format checker API

import requests

url = "https://api.apilayer.com/email_verification/check?email={shaikatmajumder010@gmail.com}"

payload = {}
headers= {
  "apikey": "aIL0QXSQ2ciNYzD3S8vs6FXN3bSwJBFh"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)

# if 200 then okay or else not okay!
print(status_code)

if(status_code == 200):
  print("Email address is valid!")

else:
  print("Invalid email address!")