import json

import requests

api_key = '3c536dd4ebee37d4a1f032c7'
api_url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"

r = requests

source_currency = input("Bozudurulacak döviz cinsi: ")  # USD
target_currency = input("İstenilen döviz cinsi: ")  # TRY
amount = int(input(f"Toplamda kaç {source_currency} bozdurmak istiyorsunuz: "))  # Kaç dolar bozdurulacak?

result = r.get(api_url + source_currency)
result_json = json.loads(result.text)

print(f"1 {source_currency} = {result_json['conversion_rates']['TRY']} {target_currency}")
print(f"{amount} {source_currency} = {amount * result_json['conversion_rates'][target_currency]} {target_currency}")
