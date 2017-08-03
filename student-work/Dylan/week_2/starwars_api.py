import requests
import json

response = requests.get("http://swapi.co/api/films/")

# print(response.status_code)

# print(response.headers)

response_dict = response.json()

# print(response_dict)


x = json.dumps(response_dict, indent=4)
# print(x)