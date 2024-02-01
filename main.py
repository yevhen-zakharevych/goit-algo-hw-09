import timeit

from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins


def main():
    time_find_coins_greedy_small = timeit.timeit(lambda: find_coins_greedy(113), number=10)
    time_find_min_coins_small = timeit.timeit(lambda: find_min_coins(113), number=10)

    time_find_coins_greedy_medium = timeit.timeit(lambda: find_coins_greedy(1_132), number=10)
    time_find_min_coins_medium = timeit.timeit(lambda: find_min_coins(1_132), number=10)

    time_find_coins_greedy_big = timeit.timeit(lambda: find_coins_greedy(10_013), number=10)
    time_find_min_coins_big = timeit.timeit(lambda: find_min_coins(10_013), number=10)

    print(find_coins_greedy(10_013))

    print(f"{'| Method': <20} | {'Time for small cost': <30} | {'Time for medium cost': <30} | {'Time for large cost': <30}")
    print(f"{'-' * 20} | {'-' * 30} | {'-' * 30} | {'-' * 30}")
    print(f"{'| find_coins_greedy': <20} | {time_find_coins_greedy_small:<30.5f} | {time_find_coins_greedy_medium:<30.5f} | {time_find_coins_greedy_big:<30.5f}")
    print(f"{'| find_min_coins': <20} | {time_find_min_coins_small:<30.5f} | {time_find_min_coins_medium:<30.5f} | {time_find_min_coins_big:<30.5f}")


if __name__ == "__main__":
    main()
