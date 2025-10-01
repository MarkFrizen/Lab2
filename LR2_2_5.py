import random

def guess_number():
    print("=== Игра 'Угадай число' ===")
    print("Я загадал число от 1 до 100. Попробуй угадать!")

    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            txt = input("Твоя догадка: ")
            if txt == "q":
                break
            guess = int(txt)
            attempts += 1

            if guess < secret_number:
                print("Слишком маленькое число! Попробуй еще.")
            elif guess > secret_number:
                print("Слишком большое число! Попробуй еще.")
            else:
                print(f"Поздравляю! Ты угадал число {secret_number} за {attempts} попыток!")
                break

        except ValueError:
            print("Пожалуйста, введите целое число!")

guess_number()