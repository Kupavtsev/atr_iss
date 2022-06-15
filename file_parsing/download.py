import requests

remote_url = 'https://iss.moex.com/iss/engines/stock/markets/shares/securities/sber.json'
local_file_name = 'sber.json'

data = requests.get(remote_url)

# Save file data to local copy
with open(local_file_name, 'wb')as file:
    file.write(data.content)