n = int(input())
lines = []
while n != 0:
    lines.append(input())
    n -= 1
l = []
dir = {}
for line in lines:
    l = line.split(';')
    if l[0] not in dir:
        games = [0, 0, 0, 0, 0]
        dir[l[0]] = games
    if l[2] not in dir:
        games = [0, 0, 0, 0, 0]
        dir[l[2]] = games
    if l[0] in dir:
        n = dir[l[0]]
        n[0] += 1
        dir[l[0]] = n
        if l[1] > l[3]:
            p = dir[l[0]]
            p[1] += 1
            p[4] += 3
            dir[l[0]] = p
        elif l[1] == l[3]:
            r = dir[l[0]]
            r[2] += 1
            r[4] += 1
            dir[l[0]] = r
        elif l[1] < l[3]:
            lose = dir[l[0]]
            lose[3] += 1
            dir[l[0]] = lose
    if l[2] in dir:
        n_1 = dir[l[2]]
        n_1[0] += 1
        dir[l[2]] = n_1
        if l[1] < l[3]:
            p_1 = dir[l[2]]
            p_1[1] += 1
            p_1[4] += 3
            dir[l[2]] = p_1
        elif l[1] == l[3]:
            r_1 = dir[l[2]]
            r_1[2] += 1
            r_1[4] += 1
            dir[l[2]] = r_1
        elif l[1] > l[3]:
            lose_1 = dir[l[2]]
            lose_1[3] += 1
            dir[l[2]] = lose_1
print(dir)
for k, v in dir.items():
    print(k + ":", end='')
    print(str(v[0]) + " " + str(v[1]) + " " + str(v[2]) + " " + str(v[3]) + " " + str(v[4]))
