import requests
import json
res = requests.get("https://catfact.ninja/fact")
print(json.dumps(res.json(), indent=2))
print(res.json())