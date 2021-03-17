def get_profit_dates(stock_prices, dts):
    min_i = 0
    min_p_i = 0
    max_p_i = 0
    for i in range(1, len(stock_prices)):
        if stock_prices[i] > stock_prices[max_p_i]:
            min_p_i = min_i
            max_p_i = i
        elif stock_prices[i] < stock_prices[min_i]:
            min_i = i
    return stock_prices[max_p_i] - stock_prices[min_p_i], dts[min_p_i], dts[max_p_i]


def test_highest_dates_found():
    stock_prices = [10, 5, 20, 32, 25, 12]
    dts = [
        '2019-01-01',
        '2019-01-02',
        '2019-01-03',
        '2019-01-04',
        '2019-01-05',
        '2019-01-06',
    ]

    highest_profit, date_buy, date_sell = get_profit_dates(stock_prices, dts)

    assert highest_profit == 27
    assert date_buy == '2019-01-02'
    assert date_sell == '2019-01-04'
