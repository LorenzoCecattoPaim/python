import requests
import json

cotacao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
cotacao = cotacao.json()
cotacao_dolar = cotacao['USDBRL']['bid']

cotacao_Euro = cotacao['EURBRL']['bid']
print(f'A cotação atual do Dólar é {cotacao_dolar}')
print(f'A cotação atual do Euro é {cotacao_Euro}')