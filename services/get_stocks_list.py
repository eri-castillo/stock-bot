import requests
import json

def get_top_ten_gainers():
    data = requests.get('https://securitiesapi.webullfintech.com/api/securities/market/v5/card/stockActivityPc.advanced/list?regionId=6&userRegionId=1&hasNum=0&pageSize=10')
    stocks = data.json()
    stocks_list = []
    for elem in stocks:
        dictionary = {
            'symbol': elem['symbol'],
            'volume': elem['volume'],
            'pChange': elem['pChange']
        }
        stocks_list.append(dictionary)

    return stocks_list

#   Get A List Of Stocks Based On Country And Exchange
def get_stocks_by_country_exchange(country, exchange):
    data = requests.get('https://api.twelvedata.com/stocks')
    stocks = data.json()
    stocks_list = []
    for stock in stocks['data']:
        if(stock['country'] == country and stock['exchange'] == exchange):
            stocks_list.append(stock['symbol'])
    return stocks_list


def get_last_five_minutes_volume(stocks_list):
    url = 'https://api.twelvedata.com/time_series?symbol={0}&interval=1min&apikey=0b1715683f9c4238afa565b67ee225c8'.format(stocks_list)
    print(url)
    data = requests.get(url)
    volume_data = data.json()
    count = 0

    for vol in volume_data['values']:
        #   Check if datetime is less than five minutes
        count += 1
        print('{}-----'.format(count))
        print(vol)