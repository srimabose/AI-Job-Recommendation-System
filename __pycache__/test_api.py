import requests

url = "http://127.0.0.1:5000/recommend"
data = {"skills": "python, machine learning"}

response = requests.post(url, json=data)

print("Response Status Code:", response.status_code)
print("Response JSON:", response.json())
