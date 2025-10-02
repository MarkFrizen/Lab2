def perform_calculation(num1: float, num2: float, operator: str) -> float:
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y if y != 0 else None,
        '^': lambda x, y: x ** y,
        '**': lambda x, y: x ** y,
        '%': lambda x, y: x % y if y != 0 else None
    }
    if operator not in operations:
        raise ValueError("Неизвестный оператор")
    result = operations[operator](num1, num2)
    if result is None:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return result
def get_number_input(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: пожалуйста, введите корректное число!")
def get_operator_input() -> str:
    valid_operators = ['+', '-', '*', '/', '^', '**', '%']
    while True:
        operator = input("Введите оператор (+, -, *, /, **, ^, %): ").strip()
        if operator in valid_operators:
            return operator
        print("Неизвестный оператор! Пожалуйста, используйте один из: +, -, *, /, **, ^, %")
def display_welcome_message():
    print("=== Простой калькулятор ===")
    print("Доступные операции: +, -, *, /, **, ^, %")
def display_result(num1: float, num2: float, operator: str, result: float):
    print(f"Результат: {num1} {operator} {num2} = {result}")
def simple_calculator():
    display_welcome_message()
    try:
        num1 = get_number_input("Введите первое число: ")
        operator = get_operator_input()
        num2 = get_number_input("Введите второе число: ")
        result = perform_calculation(num1, num2, operator)
        display_result(num1, num2, operator, result)
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")