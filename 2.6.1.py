s = -1
sq = 0
flag = 1
while s != 0:
    if flag == 1:
        s = 0
        flag = 0
    n = int(input())
    s += n
    sq += (n ** 2)
print(sq)
