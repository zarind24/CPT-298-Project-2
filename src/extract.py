import requests

DATA_URL = "https://opendata.arcgis.com/datasets/b0c7b943162f45e48b3a829b7f35709a_0.geojson"

def fetch_data():
    response = requests.get(DATA_URL)
    response.raise_for_status()
    return response.json()