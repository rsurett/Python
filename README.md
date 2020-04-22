# Python
Pull data with multiple tickers from yahoo finance.  It actually gets the data for the first ticker entered.  But I am trying to build a loop that will allow me to enter in multiple tickers and for it get the stock price X number of times for each ticker.  Right now, it only gets the data for the first ticker entered.  Its works great on that one.  Must be something wrong in mu function:

def price_tracker():
    ticker_count=-1
    for i in ticker:
