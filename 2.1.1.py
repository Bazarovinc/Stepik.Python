# put your python code here
s = input()
n = list(s)
m = []
for i in n:
    m.append(int(i))
if sum(m[0:3]) == sum(m[3:]):
    print("Счастливый")
else:
     print("Обычный")
