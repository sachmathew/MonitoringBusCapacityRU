import requests

url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"

querystring = {"agencies":"1323","callback":"call"}

headers = {
    'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
    'x-rapidapi-key': "API_KEY_HERE"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)