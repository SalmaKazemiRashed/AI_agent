import requests


## This script is for getting up-to-date value of bitcoin in terms of US dollars and Euro

url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd,eur"
response = requests.get(url)
print(response.status_code)

if response.status_code == 200:
    data = response.json()
    usd_price = data['bitcoin']['usd']
    eur_price = data['bitcoin']['eur']


print('instant bitcoin value:')
print(f"USD: { usd_price} $")
print(f"EUR: { eur_price} £")

