import json
import requests
import tokens 
x = requests.get('https://api.github.com/users',params=tokens.token) #Api Key Token (Replace tokens.token with your own access token <params = 'xyzadbz024bzs'> and delete import tokens)

print(x.status_code)
print(x.json()) #Converts the Reponse object into a json object

