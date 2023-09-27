import time
from libs.openexchange import OpenExchangeClient

APP_ID = "c18b68af98bf498798b59895015c8e0d"

client = OpenExchangeClient(APP_ID)

usd_amount = 1250  # $

for _ in range(3):
    start = time.time()
    vnd_amount = client.convert(usd_amount, "USD", "VND")
    end = time.time()

    print(end - start)

print(vnd_amount)
