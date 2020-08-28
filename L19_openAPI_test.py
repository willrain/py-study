import requests
import pprint

res = requests.get('http://api.github.com/users/willrain')

print(type(res))

pprint.pprint(res.json())

