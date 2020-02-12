# put your python code here
min = int(input())
max = int(input())
real = int(input())
if min <= real <= max:
    print("Это нормально")
elif real < min:
    print("Недосып")
elif real > max:
    print("Пересып")
