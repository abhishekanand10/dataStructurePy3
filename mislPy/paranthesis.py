s = "()]"

check = [s[0]]
l = ["{}", "()", "[]"]
lenght = len(s)

i = 1
j = 1

while len(s) > i:
    check.append(s[i])
    if check[j - 1] + check[j] in l:
        check.pop()
        check.pop()
        j = j - 1
        i = i + 1
    else:
        i = i + 1
        j = j + 1

if not check:
    print(True)
else:
    print(False)