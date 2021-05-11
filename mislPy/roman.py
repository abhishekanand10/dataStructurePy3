strs = ["hello", "hela"]

min = len(strs[0])

length = len(strs)

for k in range(1,length):
    if len(strs[k]) < min:
        min = len(strs[k])

for j in range(min):
    for i in range(1, length):
        if strs[i][j] != strs[0][j]:
            print(strs[0][:j])
            break

print(strs[0][:j])