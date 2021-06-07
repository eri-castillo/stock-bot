import os
import robin_stocks.robinhood as rh


#   Connect to Robinhood
def connect():
    print('Connecting to Robinhood...')
    user = os.environ.get("robinhood_username")
    password = os.environ.get("robinhood_password")
    rh.authentication.login(username=user,
             password=password,
             expiresIn=86400,
             by_sms=True)
    print('Connected to Robinhood')


#   Disconnect from Robinhood
def disconnect():
    print('Disconnecting from Robinhood...')
    rh.authentication.logout()
    print('Disconnected from Robinhood...')


#   Get Account Profile
def get_act_profile():
    print('Getting Account Profile...')
    profile = rh.profiles.load_account_profile()
    print(f'Profile: {profile}')


#   Get account balance
def get_cash_balance():
    print("Getting Cash Balance...")
    balance = rh.profiles.load_account_profile(info='cash')
    print(f'Balance: {balance}')


#   Buy a stock
def order_stock(symbol, qty, order_type, limit_price, stop_price, time_in_effect, extended_hours):
    print(f'{order_type}ing {qty} {symbol} for ${limit_price}')
    order_info = rh.orders.order()
    print(f'Order Info: {order_info}')


#   Cancel all stock orders


#   Get day trades
def get_day_trades():
    print('Getting Day Trades')
    day_trades = rh.account.get_day_trades()
    print(f'Day Trades: {day_trades}')


#   Get events for stock

#   Get the top 20 movers
def get_top_movers():
    print('Getting top 20 movers')
    top_movers = rh.markets.get_top_movers()
    print(f'Top 20: {top_movers}')


#   Get stocks that are currently being held
def get_held_stocks():
    print('Getting held stocks')
    current_stocks = rh.account.get_open_stock_positions()
    print(f'Stocks Held: {current_stocks}')


#   Order Buy Limit
def order_buy_limit(symbol, qty, limit_price, extended_hours):
    #gtc - good until cancelled
    #   gfd - good for the day
    limit_order = rh.orders.order_buy_limit(symbol, qty, limit_price, 'gfd', extended_hours, True)
    print(f'Limit Order Info: {limit_order}')


# Get all stock orders
