import yfinance as yf

data = yf.download('MVIS','2020-12-31','2021-05-01')

print(data)

data.to_csv('mvis_stock_prices.csv')

# data = yf.download('AMC','2020-12-01','2021-05-01')

# print(data)

# data.to_csv('amc_stock_prices.csv')

# data = yf.download('BB','2020-12-01','2021-05-01')

# print(data)

# data.to_csv('bb_stock_prices.csv')
