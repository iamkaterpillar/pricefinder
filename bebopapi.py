import requests
import pprint

resp = requests.get("https://api-uat.bebop.xyz/ethereum/v1/token-info")

print(resp.json())
# pprint.PrettyPrinter(resp.json(), indent=4)
