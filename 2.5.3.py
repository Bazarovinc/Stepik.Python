ar = [int(i)for i in input().split()]
ar_1 = []
for i in ar:
    if ar.count(i) > 1 and i not in ar_1:
        ar_1.append(i)
for i in sorted(ar_1):
    print(i, end=' ')
