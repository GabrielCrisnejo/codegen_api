import requests

API_KEY = "6W4kQKtDBgF1eF24WeiL0peP1XdcSuLgbG8G1csi" 
url = "https://api.eia.gov/v2/electricity/retail-sales/data/"

params = {
    "api_key": API_KEY,
    "frequency": "monthly",
    "data[0]": "sales",
    "facets[stateid][]": "FL",
    "start": "2024-11",
    "end": "2024-12",
    "sort[0][column]": "period",
    "sort[0][direction]": "desc",
    "offset": 0,
    "length": 5000
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error {response.status_code}: {response.text}")
