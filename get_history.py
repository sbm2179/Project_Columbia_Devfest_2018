try:
    import secret
except:
    print('keys not defined. please define variables secret_key and public_key in a file called secret.py')

from binance.client import Client
import time

def getHistory(symbol, filename, candle_size, days_ago):
    """

    symbol (str) - symbol name, ex. "XRPBTC"
    filename (str) - name of target file, ex. "XLM_BTC_1min_60day_binance_data.txt"
    candle_size (str) - candle time interval ex. '1m'
    days_ago (int) - number of days to go back to gather data

    returns - .txt file with OHLCV data

    possible intervals for candle size:

    1MINUTE  = '1m'
    3MINUTE  = '3m'
    5MINUTE  = '5m'
    15MINUTE = '15m'
    30MINUTE = '30m'
    #1HOUR    = '1h'
    2HOUR    = '2h'
    4HOUR    = '4h'
    6HOUR    = '6h'
    8HOUR    = '8h'
    12HOUR   = '12h'
    1DAY     = '1d'
    3DAY     = '3d'
    1WEEK    = '1w'
    1MONTH   = '1M'

    """
    try:
        client = Client(secret.public_key, secret.secret_key)
    except ClientAuthFailed:
        print('couldn\'t connect to client. check public/secret keys')

    print('getting data...')

    days_ago = str(days_ago) + ' days ago UTC'

    klines = client.get_historical_klines(symbol, candle_size, days_ago)

    print('data obtained.')
    print('writing data to file...')

    f = open(filename, 'w')
    f.write('UTC,time,open,high,low,close,volume')
    f.write('\n')
    f.close()

    f = open(filename, 'a')
    for kline in klines:
        time_utc   = kline[0]/1000
        time_readable = time.ctime(time_utc)
        open_price = kline[1]
        high       = kline[2]
        low        = kline[3]
        close      = kline[4]
        volume     = kline[5]

        f.write(str(time_utc))
        f.write(',')
        f.write(time_readable)
        f.write(',')
        f.write(open_price)
        f.write(',')
        f.write(high)
        f.write(',')
        f.write(low)
        f.write(',')
        f.write(close)
        f.write(',')
        f.write(volume)
        f.write('\n')
    f.close()

    print('done!')
