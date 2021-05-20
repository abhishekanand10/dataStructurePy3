# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45

    if n <= 1:
        return n

    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 45

    l = [0,1]
    if n <= 1:
        return l[n]
    for i in range(1,n):
        l.append(l[i] + l[i-1])

    return l[n]


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
