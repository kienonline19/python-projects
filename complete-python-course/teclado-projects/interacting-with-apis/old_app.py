import requests

ENDPOINT = "https://openexchangerates.org/api/latest.json"
APP_ID = "c18b68af98bf498798b59895015c8e0d"

response = requests.get(f"{ENDPOINT}?app_id={APP_ID}")

exchange_rates = response.json()["rates"]

usd_amount = 1250  # $
vnd_amount = usd_amount * exchange_rates["VND"]

print(vnd_amount)
