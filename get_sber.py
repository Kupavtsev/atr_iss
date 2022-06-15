import json
import requests

remote_url = 'https://iss.moex.com/iss/engines/stock/markets/shares/securities/sber.json'

DATA = requests.get(remote_url).json()



def get_ohlc_sber(data=DATA):

    count_columns = 0
    OHLC = {}
    for el in data['marketdata']['columns']:
        if el == "SYSTIME":
            OHLC["SYSTIME"] = count_columns
        if el == "OPEN":
            OHLC["OPEN"] = count_columns
        if el == "HIGH":
            OHLC["HIGH"] = count_columns
        if el == "LOW":
            OHLC["LOW"] = count_columns
        if el == "LAST":
            OHLC["LAST"] = count_columns
        if el == "VOLTODAY":
            OHLC["VOLTODAY"] = count_columns
        count_columns += 1

    # Finding list number with TQBR Sber data 
    x = 'TQBR'
    y = 1

    for i in data['marketdata']['data']:
        if i[1] == x:
            y += 1

    # Creating dict of OHLC Vol
    OHLC["SYSTIME"] = data['marketdata']['data'][y][OHLC["SYSTIME"]]
    OHLC["OPEN"] = data['marketdata']['data'][y][OHLC["OPEN"]]
    OHLC["HIGH"] = data['marketdata']['data'][y][OHLC["HIGH"]]
    OHLC["LOW"] = data['marketdata']['data'][y][OHLC["LOW"]]
    OHLC["LAST"] = data['marketdata']['data'][y][OHLC["LAST"]]
    OHLC["VOLTODAY"] = data['marketdata']['data'][y][OHLC["VOLTODAY"]]
  
    # print(OHLC)
    return OHLC

if __name__ == '__main__':
    get_ohlc_sber()