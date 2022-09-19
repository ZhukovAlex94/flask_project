import requests


def get_rate(currency: str) -> float | None:
    response = requests.get("https://bitpay.com/api/rates")
    data = response.json()
    data_filter = [x['rate'] for x in data if x['code'].lower() == currency.lower()]
    return data_filter[0] if len(data_filter) > 0 else None
