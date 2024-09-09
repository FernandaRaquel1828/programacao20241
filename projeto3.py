import httpx
import json

cidade = input('digite a cidade: ')
api_key = "782e25ecfb2ac8b4483207bd6e2a3161"
link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade},{br}&lang={pt_br}&appid={api_key}"


req = requests.get(link)
req_dic = req.json()
descricao = req_dic['weather']
tempertura = req_dic['main']['temp'] - 273.15
print(descricao, f'{temperatura:.2f}°c')
