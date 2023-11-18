import requests

r = requests.post('https://reqbin.com/echo/post/json')

print(r.json())