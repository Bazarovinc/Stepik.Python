s = input()
j = 0
n_str = ""
size = len(s)
while s:
    n = 0
    c = s[j]
    while j < size and s[j] == c:
        n += 1
        j += 1
    n_str += c
    n_str += str(n)
    if j == len(s):
        break
print(n_str)
