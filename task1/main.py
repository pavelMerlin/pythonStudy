import math
import random
import time


# \033[4m — подчёркнутый;
# \033[37m — белая надпись;
# \033[44m — синий фон;
# {} — заменится на «Python 3»;
# \033[0m — сброс к начальным значениям.
# \033[31m - red

# Convert radians to degrees and vice versa
def degree_swap():
    # num which user write in console (deg or rad); convert_num - is solve
    user_num, convert_num = 0, 0

    while True:
        # show txt info in console
        print("Добро пожаловать в перевод градусов!\n"
              "\nВведите \"R\" если вы хотите перевести радианы в градусы"
              "\nВведите \"P\" если вы хотите перевести грудусы в радианы")

        # take user info
        choise = input()

        # R - deg to rad; P - rad to deg; else - error
        if choise == 'R':
            user_num = int(input("Введите радианы: "))
            convert_num = math.degrees(user_num)
            break
        elif choise == 'P':
            user_num = int(input("Введите градусы: "))
            convert_num = math.radians(user_num)
            break
        else:
            print("Вы неверно выполнили условия выше!")

    # final result with round to two symbols after dot
    print(round(convert_num, 2))

    # waiting for maim screen
    time.sleep(3)


# communal services calculator
def communal_services():
    # list with future prices
    tariffs = []
    # dictionary with communal services names
    communal_names = {1: 'за газ', 2: 'за воду', 3: 'за электроэнергию'}

    # cycle for random tariff prices
    for _ in range(3):
        tariffs.append(round(random.uniform(0.1, 0.9), 2))

    # take user choice
    user_choose = int(input("НУ привет, должничок...\n"
                            "За что платим?\n\n"
                            f"1 - за газ;\t ТАРИФ: {tariffs[0]}\n"
                            f"2 - за воду;\t ТАРИФ: {tariffs[1]}\n"
                            f"3 - за электроэнергию;\t ТАРИФ: {tariffs[2]}\n"))

    # cycle for errors with user input
    while True:
        # utility user info
        before_utility = float(input(f"\033[33mВведите предыдущие данные {communal_names[user_choose]} с счетчика: "))
        active_utility = float(input(f"\n\033[34mВведите нынешние данные {communal_names[user_choose]} с счетчика: "))

        if before_utility > active_utility:
            print("\033[4m\033[37mПредыдущие значения не должны быть меньше нынешних!\033[0m")
            continue
        else:
            break

    # calculating utility bills with tariff prices
    bill = (active_utility - before_utility) * tariffs[user_choose - 1]

    # spaces
    print("\n" * 3)

    # final info
    print("Чек:\n"
          f"Предыдущие показания {before_utility}\n"
          f"Нынишние показания {active_utility}\n"
          f"Тариф {communal_names[user_choose]} {tariffs[user_choose - 1]}\n\n"
          f"\t\033[4m\033[31mК оплате {bill}$\n\033[0m")

    # waiting for maim screen
    time.sleep(3)


while True:
    # start screen to choose the program
    programChose = input("Выберите программу:\n"
                         "0. Выйти\n"
                         "1. Радианты в валорантов\n"
                         "2. Комуналка\n")

    if programChose == '0':
        break
    elif programChose == '1':
        degree_swap()
        continue
    elif programChose == '2':
        communal_services()
        continue

