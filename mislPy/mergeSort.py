def mergesort(a):
    if len(a) == 1:
        return
    else:
        # tmp = []
        mid = len(a) // 2

        ll = a[:mid]
        rr = a[mid:]

        mergesort(ll)
        mergesort(rr)

        merge(a, ll, rr)

    return a


def merge(a, leftlist, rightlist):

    ln = len(leftlist)
    rn = len(rightlist)

    x = y = z = 0

    while x < ln and y < rn:
        if leftlist[x] <= rightlist[y]:
            a[z] = leftlist[x]
            x += 1
        else:
            a[z] = rightlist[y]
            y += 1
        z += 1

    if x < len(leftlist):
        for i in range(x, ln):
            a[z] = leftlist[x]
            z += 1
            x += 1
    elif y < len(rightlist):
        for i in range(y, rn):
            a[z] = rightlist[y]
            z += 1
            y += 1


if __name__ == '__main__':
    lst = [7, 5, 1, 3, 2]
    print(mergesort(lst))
