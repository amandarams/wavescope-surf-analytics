import requests #Biblioteca que permite conversar com a API #GET = “API, me dê essas informações.”

from typing import NamedTuple


class Saquarema(NamedTuple):

    latitude: float
    longitude: float

saquarema = Saquarema(-22.92,-42.51)

parametros = {
    "latitude": saquarema.latitude,
    "longitude": saquarema.longitude,
    "hourly": "wave_height"
}

print(parametros)

url = "https://marine-api.open-meteo.com/v1/marine"
resposta = requests.get(url, params=parametros)

print(resposta.status_code)

dados = resposta.json()
print(dados["hourly"])