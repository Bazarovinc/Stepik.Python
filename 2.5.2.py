# put your python code here
ar = [int(i)for i in input().split()]
for i in range(len(ar)):
    if len(ar) == 1:
        s = ar[i]
    elif i == 0:
        s = ar[i + 1] + ar[-1]
    elif i == len(ar) - 1:
        s = ar[0] + ar[i - 1]
    else:
        s = ar[i - 1] + ar[i + 1]
    print(s)
