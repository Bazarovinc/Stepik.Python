s = input()
size = len(s)
s = s.lower()
n = 0
n += s.count('g')
n += s.count('c')
print((n / size) * 100)
