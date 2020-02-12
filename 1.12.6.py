# put your python code here
n = int(input())
if 11 <= n <= 14 or  11 <= n % 100 <= 14:
     print(n, "программистов")
elif 1 < n % 10 < 5:
    print(n, "программиста")
elif n % 10 == 1:
    print(n, "программист")
elif n % 10 >= 5 or n % 10 == 0:
    print(n, "программистов")
