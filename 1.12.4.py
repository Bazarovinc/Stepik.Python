# put your python code here
str = input()
if str == 'прямоугольник':
    a = int(input())
    b = int(input())
    print(a * b)
elif str == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(s)
elif str == 'круг':
    a = int(input())
    s = 3.14 * (a ** 2)
    print(s)
