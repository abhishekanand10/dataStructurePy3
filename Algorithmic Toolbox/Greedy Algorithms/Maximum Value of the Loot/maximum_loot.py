# python3
import collections
from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    valDict = {}
    c = capacity
    val = 0
    for i in range(len(weights)):
        item[i] = (prices[i], weights[i], prices[i]//weights[i])

    # item.sort(Key)
    item.sort(key=lambda e: e.val)

    for x in item:
        print(x)



        #
        # if c - weights[-1*i] >= 0:
        #     c -= weights[-1*i]
        #     val += weights[-1*i] * prices[-1*i]
        # elif c - weights[-1*i] < 0:
        #     val += c * prices[-1*i]
        #     return val




if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    # opt_value = \
    maximum_loot_value(input_capacity, input_weights, input_prices)
    # print("{:.10f}".format(opt_value))

