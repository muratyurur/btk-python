import json

import requests

result = requests.get('https://jsonplaceholder.typicode.com/todos')
result = result.text
result = json.loads(result)

for i in result:
    if i['userId'] == 1:
        print(i['title'])
