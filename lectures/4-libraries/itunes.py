import json
import requests
import sys

if len(sys.argv) != 2:
    sys.exit("1 argument expected")

response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=50&term={sys.argv[1]}")

# print(json.dumps(response.json(), indent=2))

o = response.json()
for result in o["results"]:
    print(result["trackName"])
