coins = [50, 25, 10, 5, 2, 1]


def find_coins_greedy(cost):
    res_coins = {}
    for coin in coins:
        count = cost // coin
        if count > 0:
            res_coins[coin] = count
            cost -= count * coin
    return res_coins


if __name__ == '__main__':
    print(find_coins_greedy(115))
