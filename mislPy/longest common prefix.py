strs = ["hello", "hella", "hela"]
prefix = ""

if not strs:
    print(prefix)

min_len = min([len(s) for s in strs])
print(min_len)

for i in range(min_len):

    d = all([s[i] == strs[0][i] for s in strs])
    print(d)

print(prefix)