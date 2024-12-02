import requests
import os
from datetime import datetime, timedelta
import time

API_KEY = os.getenv('API_KEY')
BASE_URL = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

headers = {
    'X-CMC_PRO_API_KEY': API_KEY,
    'Accept': 'application/json',
}

params = {
    'convert': 'USD',
}

def get_bitcoin_price():
    response = requests.get(BASE_URL, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        bitcoin_data = next(item for item in data['data'] if item['symbol'] == 'BTC')
        return bitcoin_data['quote']['USD']['price']
    else:
        print(f'Erro ao obter os dados: {response.status_code} - {response.text}')
        return None

initial_price = get_bitcoin_price()
if initial_price is not None:
    print(f'O preço inicial do Bitcoin é: ${initial_price:.2f}')

    time.sleep(160)  # em segundos

    new_price = get_bitcoin_price()
    if new_price is not None:
        print(f'O preço do Bitcoin após 2 minutos é: ${new_price:.2f}')

        # Calculando a variação
        variation = new_price - initial_price
        print(f'A variação do preço do Bitcoin em 2 minutos foi: ${variation:.2f}')
else:
    print('Não foi possível obter o preço inicial do Bitcoin.')
