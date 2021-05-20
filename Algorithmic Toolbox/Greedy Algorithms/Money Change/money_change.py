# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    t = 0 # total change count
    den = [10,5,1]
    i = 0 #counter for den


    while money >0:
        t += int(money / den[i])
        money %= den[i]
        i += 1

    return t


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
