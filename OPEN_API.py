import requests

url = "https://transloc-api-1-2.p.rapidapi.com/routes.json"

querystring = {"agencies":"1323","callback":"call"}

headers = {
    'x-rapidapi-host': "transloc-api-1-2.p.rapidapi.com",
    'x-rapidapi-key': "76fcb78df0msh00bdccc4dee6f53p1e9467jsne2d32902a421"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)