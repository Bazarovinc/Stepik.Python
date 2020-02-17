def read_lines(n):
    lines = []
    while n != 0:
        lines.append(input())
        n -= 1
    return (lines)


d = int(input())
dictionary = read_lines(d)
l = int(input())
lines = read_lines(l)
printed = []
for line in lines:
    words = line.split()
    for word in dictionary:
        for w in words:
            if w.lower() == word.lower():
                words.remove(w)
    for w in words:
        if w.lower() not in printed:
            print(w)
            printed.append(w.lower())
