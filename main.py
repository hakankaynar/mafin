from strategy1 import calculate
from user import User




def old_main(tickers, period, interval):
    buy_tickers = []

    for ticker in tickers:
        try:
            result = calculate(ticker, period, interval)
            if result is True:
                buy_tickers.append(ticker)
        except:
            print("Something went wrong with " + ticker)

        #print("==================================================================")

    for ticker in buy_tickers:
        print(ticker + " is BUY")


if __name__ == '__main__':
    users = User.get_users()

    for a_user in users:
        for a_calculation in a_user.calculations:
            print("==================================================================")
            print(a_user.username + " " + a_calculation.period + " " + a_calculation.interval + " calculation")
            print("==================================================================")
            print("==================================================================")
            old_main(a_user.tickers, a_calculation.period, a_calculation.interval)
