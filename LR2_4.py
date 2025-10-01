import math
a = int(input("Введите 1-е число: "))
b = int(input("Введите 2-е число: "))
gcd = math.gcd(a, b)
print(f"НОД({a}, {b}) = {gcd}")