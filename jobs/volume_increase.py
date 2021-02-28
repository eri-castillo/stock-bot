import yfinance as yf
import pandas as pd


# stock_symbols = ['SPOT', 'AGNC','BTG', 'GE', 'NIO', 'SDC']
#
# incr_symbols = []
#
# for stock in stock_symbols:
#     # print(stock)
#     try:
#         stock_info = yf.Ticker(stock)
#         hist = stock_info.history(period="5d")
#         prev_avg_vol = hist['Volume'].iloc[1:4:1].mean()
#         print('prev avg vol: '+str(prev_avg_vol))
#         tod_vol = hist['Volume'][-1]
#         print('todays vol: ' + str(tod_vol))
#         if tod_vol > prev_avg_vol * 2:
#             incr_symbols.append(stock)
#     except:
#         pass
#
# print(incr_symbols)