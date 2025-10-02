import math
def calculate_gcd(num1, num2):
    return math.gcd(num1, num2)
def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")
def get_gcd():
    first_number = get_number_input("Введите первое число: ")
    second_number = get_number_input("Введите второе число: ")
    gcd_result = calculate_gcd(first_number, second_number)
    print(f"НОД({first_number}, {second_number}) = {gcd_result}")