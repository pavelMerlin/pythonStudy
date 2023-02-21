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


# tax services calculator
def tax_calculator():
    # take user income
    income = float(input("\033[37mДобро пожаловать в налоговую!\n"
                         "Сколько денег Вам пришло на счет?\n"
                         "\033[4mЗначение: \033[0m"))

    # generate tax value
    tax_value = round(random.uniform(0.3, 1.5), 2)
    print(f"\nПроцент налога \033[31m{tax_value}%\033[0m")

    # 10 * (1 / 100) = 0,1 the tax price
    stole_money = income * (tax_value / 100)

    # income 10 - 0,1 = 9,9; real user income
    real_income = income - stole_money

    # final user info
    print("\n\033[37mИтого: \n"
          f"\tВам нужно оплатить \033[31m{round(stole_money, 2)}$\033[37m налога\n"
          f"\tВаш остаток \033[31m{round(real_income, 2)}$\033[0m\n")

    # waiting for the main screen
    time.sleep(5)


# oil calculator
def oil_calculator():
    # consumption per 100 kilometers
    consumption = float(input("\033[37mПривет странник!\n"
                              "Масло считаем?? Ну ладно... \n"
                              "Сколько кобылка ест на 100км?\n"
                              "\033[4mЗначение: \033[0m"))

    # journey range
    journey_range = float(input("\n\033[37mКак далеко едешь?\n"
                                "\033[4mЗначение:\033[0m "))

    # generate how much does oil costs
    oil_cost = round(random.uniform(1.3, 2.1), 2)

    # count our journey cost
    journey_price = (consumption * oil_cost) * journey_range / 100

    # print our info about journey price
    print("\nДалеко заедешь...\n"
          f"\t\033[31mСолярка по {oil_cost}$\033[0m\n"
          f"\t\033[31mПоездка будет стоить {journey_price}$\033[0m\n")

    # waiting for the main screen
    time.sleep(5)


# cycle for user tries
while True:
    # start screen to choose the program
    programChose = input("\nВыберите программу:\n"
                         "\t0. Выйти\n"
                         "\t1. Радианты в валорантов\n"
                         "\t2. Комуналка\n"
                         "\t3. Налоги\n"
                         "\t4. Бензоподсчет\n")

    # analyze user choice
    if programChose == '0':
        break
    elif programChose == '1':
        degree_swap()
        continue
    elif programChose == '2':
        communal_services()
        continue
    elif programChose == '3':
        tax_calculator()
        continue
    elif programChose == '4':
        oil_calculator()
        continue
