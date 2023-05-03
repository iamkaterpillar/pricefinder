import requests
import pprint

pp = pprint.PrettyPrinter(indent=1)

resp = requests.get("https://api-uat.bebop.xyz/ethereum/v1/token-info")

pp.pprint(resp.json())
