import time
from triangle_logic import *
from data import *


def detect_words(re_input_side, re_input_deg):
    """
    В этой функции мы убираем любые ошибки ввода и находим ключевые слова
    :param re_input_side: ввод сторо от юзера
    :param re_input_deg: ввод углов от юзера
    :return: ничего
    """
    for i in range(len(re_input_side)):
        detect_word_s = "сторона" in re_input_side[i]
        if detect_word_s is True:
            re_input_side.pop(i)
            return re_input_side
        else:
            try:
                re_input_side[i] = float(re_input_side[i])
            except:
                print("\033[31m\033[4mОшибка ввода сторон\033[0m")
                re_input_deg.clear()
                re_input_side.clear()
                main_screen()

    for i in range(len(re_input_deg)):
        detect_word_d = "угол" in re_input_deg[i]
        if detect_word_d is True:
            re_input_deg.pop(i)
            return re_input_deg
        else:
            try:
                if re_input_deg[i] == "":
                    re_input_deg.clear()
                    break
                re_input_deg[i] = float(re_input_deg[i])
            except:
                print("\033[31m\033[4mОшибка ввода углов\033[0m")
                re_input_deg.clear()
                re_input_side.clear()
                main_screen()


# реюзаюильность / 100+ строк / класс


def main_screen():
    """
    Вызываем мейн скрин и устанавливаем имя
    :return: попу
    """
    sides.clear()
    degs.clear()

    user_name = random.choice(user_names)
    user_rang = random.choice(user_rangs)

    user_input_side = input(f"\n\033[37mПривет \033[31m{user_rang} {user_name}\033[37m\n"
                            f"Тут мы считаем возможность существования твоем мамы\n"
                            f"Введи стороны треугольника в формате (сторона A, сторона B или сторона C или H для "
                            f"ручного ввода)\n"
                            f">>> ")

    if user_input_side == 'H':
        user_input_side = user_input_side.replace("H", "")
        print("\nРучной ввод сторон\n"
              "Введите указаную сторону или пропустите нажав Enter\n")
        for i in ["A", "B", "C"]:
            hand_input = input(f"Введите сторону {i} или Enter\n"
                               f">>> ")
            if i == "C":
                user_input_side += f"{hand_input}"
            elif hand_input != "":
                user_input_side += f"{hand_input} "

    user_input_deg = input(f"Введи углы треугольника в формате (угол Aльфа, угол Бета или угол Джета(сигма)) "
                           f"или нажми Enter или H для ручного ввода\n"
                           f">>> ")

    if user_input_deg == 'H':
        user_input_deg = user_input_deg.replace("H", "")
        print("\nРучной ввод сторон\n"
              "Введите указаный угол или пропустите нажав Enter\n")
        for i in ["A", "B", "J"]:
            hand_input = input(f"Введите угол {i} или Enter\n"
                               f">>> ")
            if i == "J":
                user_input_deg += f"{hand_input}"
            elif hand_input != "":
                user_input_deg += f"{hand_input} "

    re_input_side = user_input_side.split(" ")
    re_input_deg = user_input_deg.split(" ")

    detect_words(re_input_side, re_input_deg)

    for i in re_input_side:
        sides.append(i)
    for i in re_input_deg:
        degs.append(i)


def solve():
    solve_dic = []

    if len(sides) == 2 and len(degs) == 1:
        solve_dic.append("\t\033[0mВведи 1 - Вы можете решить по теореме косинусов\033[37m\n")

    if len(sides) == 1 and len(degs) == 2:
        solve_dic.append("\t\033[0mВведи 2 - Вы можете решить по теореме синусов\033[37m\n")

    if len(sides) == 2 and len(degs) == 1:
        if degs[0] >= 90:
            solve_dic.append("\t\033[0mВведи 3 - Вы можете решить по теореме Пифагора\033[37m\n")

    if len(sides) == 3 and len(degs) >= 0:
        solve_dic.append("\t\033[0mВведи 4 - Вы можете найти периметр\033[37m\n")
        solve_dic.append("\t\033[0mВведи 5 - Вы можете найти все углы в треугольнике\033[37m\n")

    if len(sides) == 3 and len(degs) >= 0 and len(h) != 1:
        solve_dic.append("\t\033[0mВведи 6 - Вы можете найти высоту\033[37m\n")

    print("\nДано:")
    for i in range(len(sides)):
        print(f"\033[37m{i + 1}) сторона равна \033[31m{sides[i]}\033[37m")
    for i in range(len(degs)):
        print(f"\033[37m{i + 1}) угол равен \033[31m{degs[i]}\033[37m")
    for i in range(len(h)):
        print(f"\033[37mВысота равена \033[31m{round(h[i], 2)}\033[37m")

    time.sleep(2)

    print("\nКак вы хотите решить задачу?\nИсходя из Ваших данных вот возможные действия\n\n")

    time.sleep(3)

    for i in solve_dic:
        print(i)
    if len(solve_dic) == 0:
        print("\n\033[31m\033[4mС Вашими данными невозможно корректно выполнить ни одну операцию\n\033[37m")
        main_screen()

    user_choice = input(">>> ")

    if user_choice == '1':
        a_b_cosj()
    elif user_choice == '2':
        a_sina_sinb()
    elif user_choice == '3':
        pifagor()
    elif user_choice == '4':
        perimetr()
    elif user_choice == '5':
        deg_find()
    elif user_choice == '6':
        height()
    else:
        print("\n\033[0mНевозможно\n")
        solve()


if __name__ == '__main__':
    main_screen()
    user_data = False
    for _ in range(100):

        triangle_existence()
        solve()



