ar = [int(i) for i in input().split()]
n = int(input())
s = []
i = 0
while i < len(ar):
    if ar[i] == n:
        s.append(i)
    i += 1
if len(s) == 0:
    print("Отсутствует")
else:
    for num in s:
        print(num, end=' ')
