def generate_squares_dict(start: int = 1, end: int = 10) -> dict:
    return {x: x**2 for x in range(start, end + 1)}
def print_squares(squares_dict: dict, title: str = None) -> None:
    if title:
        print(title)
    for number, square in squares_dict.items():
        print(f"  {number}² = {square}")
def pow():
    squares = generate_squares_dict(1, 10)
    print_squares(squares, "Квадраты чисел от 1 до 10:")