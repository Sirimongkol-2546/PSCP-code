"""CoinChangev1"""
def main():
    """input"""
    coin = int(input())
    coin_25, coin_left = divmod(coin, 25)
    coin_10, coin_left = divmod(coin_left, 10)
    coin_5, coin_1 = divmod(coin_left, 5)

    print(coin_25 + coin_10 + coin_5 + coin_1)
main()
