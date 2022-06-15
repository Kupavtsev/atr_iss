import requests

# All TRADES
# https://iss.moex.com/iss/engines/stock/markets/shares/securities/sber/trades.json

URL = 'https://iss.moex.com/iss/engines/stock/markets/shares/securities/sber.json'
HEADERS = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "ru",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }


responce = requests.get(url=URL, headers=HEADERS)

if responce.status_code != 200:
    raise ValueError(f"Request failed {responce.status_code}")
resp_json_content = responce.content

# SAVE TO FILE
sourceFile = open('sber.json', 'w')
print('sber.json', resp_json_content, file = sourceFile)
sourceFile.close()