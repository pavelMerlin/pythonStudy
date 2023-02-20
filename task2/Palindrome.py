import time


# cycle for users tries
while True:
    # main screen and user palindrome
    user_palindrome = input("Привет ЛОХ... хахахахах\n"
                            "ладно...\n"
                            "введи мне палинdrом\n"
                            ">>> ")

    # revers user input
    reversed_palindrome = user_palindrome[::-1]

    # check if reversed palindrome match to user input
    if reversed_palindrome == user_palindrome:
        # print congrats
        print("\033[44mПоздравляю, козаче\n"
              f"у вас - палинdrом {user_palindrome}.")
        break
    else:
        # print fail
        print(f'\033[37mОй ой ой... \n'
              f'ну и дела... это - {user_palindrome} не палинdrом...\n'
              'попробуй что-то другое.\n')

        # waiting for user analiz
        time.sleep(2)
        continue
