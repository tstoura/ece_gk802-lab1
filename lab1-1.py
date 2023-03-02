import requests
import time

url = input('Give me a url: ')

serv = None
with requests.get(url) as response:
    hdrs = response.headers.items()
    print('Headers:')
    for key,value in hdrs:
       print("{:30s} {}".format(key,value))
       if key=="Server":
           serv = value

    if serv is not None:
        print()
        print("Server:" +serv)

    print()
    print("Cookies")
    for key,value in enumerate(response.cookies):
        print("Name:{}   Expires in {} days".format(value.name,round((value.expires-time.time())/86400)))
