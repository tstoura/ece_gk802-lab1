import requests

url = input("Give me a url: ")

with requests.get(url) as response:
    html = response.text

print(response.headers)
