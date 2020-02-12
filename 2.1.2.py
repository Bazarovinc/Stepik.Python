# put your python code here
a = int(input())
b = int(input())
i = max(a, b)
while i != a * b:
    if i % a == 0 and i % b == 0:
        break
    i += 1
print(i)
