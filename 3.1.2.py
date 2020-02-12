def modify_list(l):
    ar = []
    for i in l:
        if i % 2 == 0:
            ar.append(i // 2)
    l.clear()
    for i in ar:
        l.append(i)
