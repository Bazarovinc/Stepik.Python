n = int(input())
s = []
i = 0
k = 1
while i < n:
    j = 0
    while i < n and j < k:
        s.append(k)
        j += 1
        i += 1
    k += 1
for i in s:
    print(i, end=' ')
