from yahooquery import Ticker
import json, time, sched, os


s = sched.scheduler(time.time, time.sleep)

def getStockData(): 
    stockList = ''
    stocks = ['AAPL', 'FIT', 'SNAP', 'MSFT', 'TSLA', 'AMD', 'SPOT', 'AMC']

    for data in stocks:
        ticker = Ticker(data)

        response = json.dumps(ticker.financial_data)
        responseJson = json.loads(response).get(data)

        currentPrice = float(round(responseJson.get('currentPrice'), 2))
        stockList = stockList + "%s: %s" % (data, currentPrice) + '\n'
        
    os.system('clear')

    print(stockList)
    stockList = ''
    s.enter(1, 1, getStockData)

s.enter(0, 1, getStockData)
s.run()
