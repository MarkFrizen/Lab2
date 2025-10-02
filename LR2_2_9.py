def recursive_sum(n: int) -> int:
    if n < 0:
        raise ValueError("n должно быть неотрицательным числом")
    elif n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)
def digit_sum():
    test_cases = [5, 10, 100, 0]
    for n in test_cases:
        try:
            result = recursive_sum(n)
            print(f"Сумма чисел от 1 до {n} = {result}")
        except ValueError as e:
            print(f"Ошибка для n={n}: {e}")
        except RecursionError:
            print(f"Ошибка для n={n}: превышена глубина рекурсии")