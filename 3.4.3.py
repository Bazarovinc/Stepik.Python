filename = "dataset_3363_4.txt"
d = {}
with open(filename, 'r') as f_o:
    lines = f_o.readlines()
l = []
for line in lines:
    l += line.split(";")
i = 0
d = {}
math = 0
phis = 0
rus = 0
while i != len(l):
    if i == 0 or i % 4 == 0:
        d[l[i]] = int(l[i + 1])
        math += int(l[i + 1])
        d[l[i]] += int(l[i + 2])
        phis += int(l[i + 2])
        d[l[i]] += int(l[i + 3])
        rus += int(l[i + 3])
        d[l[i]] /= 3
    i += 1
math /= len(d)
phis /= len(d)
rus /= len(d)
f = open("mid.txt", 'w')
for k, v in d.items():
    f.write(str(v))
    f.write("\n")
f.write(str(math) + " " + str(phis) + " " + str(rus))