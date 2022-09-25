import json
import requests

x = requests.get('https://api.github.com/users',params='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')

print(x.status_code)
print(x.json())

