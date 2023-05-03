import requests
import pprint

pp = pprint.PrettyPrinter(indent=1)

# This is us setting up the parameters in Python

params123 = {
    "sellToken": 'DAI' ,
    "buyToken": 'WETH' ,
    "sellAmount": str(100000 * 10**18) ,
    
}

resp = requests.get("https://api.0x.org/swap/v1/quote", params=params123, timeout=2.50)

parseresponse = resp.json()

# pp.pprint(parseresponse)
p=float(parseresponse['price'])
print(1/p)

# Hello git