lst = input().split()
for i in range(len(lst)):
    lst[i] = lst[i].lower()
d = {}
for word in lst:
    if word in d:
        n = d[word]
        n[0] += 1
        d[word] = [n[0]]
    else:
        n = 1
        d[word] = [n]

for key, values in d.items():
    print(key, values[0])
