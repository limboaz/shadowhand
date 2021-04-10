# import yfinance as yf

# data = yf.download('GME','2020-12-01','2021-03-31')

# print(data)

# data.to_csv('gme_stock_prices.csv')
# import yfinance as yf

# data = yf.download('AMC','2020-12-01','2021-03-31')

# print(data)

# data.to_csv('amc_stock_prices.csv')
import yfinance as yf

data = yf.download('BB','2020-12-01','2021-03-31')

print(data)

data.to_csv('bb_stock_prices.csv')