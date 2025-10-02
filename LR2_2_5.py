import random
MIN_NUMBER = 1
MAX_NUMBER = 100
def get_user_input():
    while True:
        try:
            txt = input("Твоя догадка: ")
            if txt.lower() == "q":
                return None
            guess = int(txt)
            if MIN_NUMBER <= guess <= MAX_NUMBER:
                return guess
            else:
                print(f"Пожалуйста, введите число от {MIN_NUMBER} до {MAX_NUMBER}.")
        except ValueError:
            print("Пожалуйста, введите целое число!")
def play_game():
    print("=== Игра 'Угадай число' ===")
    print(f"Я загадал число от {MIN_NUMBER} до {MAX_NUMBER}. Попробуй угадать!")
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0
    while True:
        user_guess = get_user_input()
        if user_guess is None:
            print("Игра окончена.")
            break
        attempts += 1
        if user_guess < secret_number:
            print("Слишком маленькое число! Попробуй еще.")
        elif user_guess > secret_number:
            print("Слишком большое число! Попробуй еще.")
        else:
            print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
            break
def game_count():
    while True:
        play_game()
        replay = input("Хочешь сыграть ещё раз? (да/нет): ").lower()
        if replay != "да":
            print("До новых встреч!")
            break