def make_list(line):
    list = []
    for i in line:
        list.append(i)
    return list


def print_cipher(line, value, key):
    for l in line:
        i = 0
        while i < len(value):
            if l == value[i]:
                print(key[i], end='')
                break
            i += 1

line_1 = input()
line_2 = input()
line_3 = input()
line_4 = input()
letters = make_list(line_1)
key = make_list(line_2)
print_cipher(line_3, letters, key)
print()
print_cipher(line_4, key, letters)
