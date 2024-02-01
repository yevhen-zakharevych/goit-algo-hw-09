coins = [50, 25, 10, 5, 2, 1]


def find_min_coins(cost):
    min_coins = [0] + [float("inf")] * cost
    last_coin_used = [0] * (cost + 1)

    for s in range(1, cost + 1):
        for coin in coins:
            if s >= coin and min_coins[s - coin] + 1 < min_coins[s]:
                min_coins[s] = min_coins[s - coin] + 1
                last_coin_used[s] = coin

    count_coins = {}
    current_cost = cost

    while current_cost > 0:
        coin = last_coin_used[current_cost]
        count_coins[coin] = count_coins.get(coin, 0) + 1
        current_cost -= coin

    return count_coins


if __name__ == "__main__":
    print(find_min_coins(113))
