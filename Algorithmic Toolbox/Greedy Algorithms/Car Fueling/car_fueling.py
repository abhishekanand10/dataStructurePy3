# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    stops.insert(0, 0)

    f = m   # check current fuel level
    refill = 0  # count of number of refills
    n = len(stops)  # still need to check for pt B
    stops.append(d)
    for i in range(1, n):
        f -= stops[i] - stops[i-1]
        if f == 0:
            f = m
            refill += 1
        elif f < 0:
            f = m - (stops[i] - stops[i-1])
            refill += 1

    if f >= 0 and stops[-1]-stops[-2] <= f:
        return refill
    elif 0 <= f < stops[-1] - stops[-2] <= m:
        refill += 1
        return refill
    elif f < 0 or stops[-1]-stops[-2] > m:
        return -1


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
