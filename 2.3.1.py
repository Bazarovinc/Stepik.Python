# put your python code here
a = int(input())
b = int(input())
c = int(input())
d = int(input())
i = c
print(' \t', end='')
while i <= d:
    print(i, end = '\t')
    i += 1
print()
for i in range(a, b + 1, 1):
    print(i, end='\t')
    for j in range(c, d + 1, 1):
        print(i * j, end = '\t')
    print()
