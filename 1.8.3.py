# put your python code here
min = int(input())
g_h = int(input())
g_min = int(input())

g_h += min // 60
if (g_min + min % 60) > 60:
    g_h += 1
    g_min = (g_min + min % 60) - 60
else:
    g_min += min % 60
print(g_h)
print(g_min)
