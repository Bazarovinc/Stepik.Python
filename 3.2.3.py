n = int(input())
d = {}
for i in range(n):
    num = int(input())
    if num in d:
        print(d[num][0])
    else:
        d[num] = [f(num)]
        print(d[num][0])
