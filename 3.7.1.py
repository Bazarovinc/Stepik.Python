n = int(input())
lines = []
while n != 0:
    lines.append(input())
    n -= 1
l = []
for line in lines:
    l = line.split(';')
    print (l)
print(lines)