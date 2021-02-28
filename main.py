from services.get_stocks_list \
    import get_stocks_by_country_exchange, \
    get_last_five_minutes_volume, \
    get_top_ten_gainers


def main():
    # #   1. Get a list of the stocks on the exchange
    # list = get_stocks_by_country_exchange('United States', 'NYSE')
    #
    # for stock in list:
    #     get_last_five_minutes_volume(stock)


    #   Get the top ten stocks
    stocks = get_top_ten_gainers()
    print(stocks)

if __name__ == '__main__':
    main()