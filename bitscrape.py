if __name__ == '__main__':
    main()

def main():
    '''My main btc scrape'''
    from urllib import request
    import json
  
    url =' https://api.coindesk.com/v1/bpi/currentprice/GBP.json'      
    header = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'} 
    req = request.Request(url, header=header)
    with request.urlopen(req) as data:
    jdata = json.load(data)
