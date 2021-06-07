import os
from services.robinhood.robinhood_apis \
    import connect, disconnect, get_act_profile, \
    get_cash_balance, get_top_movers, get_day_trades, \
    get_held_stocks


def main():
    try:

        while True:

        print('Starting bot')
        connect()
        # get_act_profile()
        get_cash_balance()
        # get_top_movers()
        # get_day_trades()
        get_held_stocks()
        disconnect()
    except KeyError as ke:
        print(ke)
    except:
        print('other error')


if __name__ == '__main__':
    main()