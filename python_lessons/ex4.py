import requests

url = "https://api-ninjas.com/api/recipe"

content = {
    'name': 'John',
    'email': "join@smth.com"
    }

requests.post(url, content)