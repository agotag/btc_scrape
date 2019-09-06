from urllib import request
import json
from pprint import pprint
from datetime import datetime
import sqlite3
import time


url =' https://api.coindesk.com/v1/bpi/currentprice/GBP.json'      
header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'} 

def __main__():

    while True:
        req = request.Request(url, headers=header)
        with request.urlopen(req) as data:
             jdata = json.load(data)
             
             dt = jdata['time']['updateduk']
             dt = datetime.strptime(dt, '%b %d, %Y at %H:%M BST')
             rate = jdata['bpi']['GBP']['rate_float']
             conn = sqlite3.connect(r'.\crypto')
             c = conn.cursor()
             param = (dt, 'GBP', rate)
             c.execute('insert into BTC (pricedate, currency, rate) values (?, ?, ?)', param)
             conn.commit()
             conn.close()
             time.sleep(60)

if __name__ == __main__:
    __main__()


