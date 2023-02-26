import random
import math
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
                print("Ошибка ввода сторон")
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
                re_input_deg[i] = float(re_input_deg[i])
            except:
                print("Ошибка ввода углов")
                re_input_deg.clear()
                re_input_side.clear()
                main_screen()


# реюзаюильность / 100+ строк / класс

def main_screen():
    """
    Вызываем мейн скрин и устанавливаем имя
    :return: попу
    """
    user_name = random.choice(user_names)
    user_rang = random.choice(user_rangs)

    user_input_side = input(f"\033[37mПривет \033[31m{user_rang} {user_name}\033[37m\n"
                            f"Тут мы считаем возможность существования твоем мамы\n"
                            f"Введи стороны треугольника в формате (сторона A, сторона B или сторона C)\n")

    user_input_deg = input(f"Введи углы треугольника в формате (угол Aльфа, угол Бета или угол Джета(сигма)) "
                           f"или нажми Enter\n")

    re_input_side = user_input_side.split(" ")
    re_input_deg = user_input_deg.split(" ")

    if len(re_input_side) > 3 or len(re_input_deg) > 3:
        print("Ошибка ввода")
        main_screen()
    elif len(re_input_side) == 0:
        print("Ошибка ввода")
        main_screen()
    elif len(re_input_side) == 1 and len(re_input_deg) < 0:
        print("Ошибка ввода")
        main_screen()

    detect_words(re_input_side, re_input_deg)

    for i in re_input_side:
        sides.append(i)
    for i in re_input_deg:
        degs.append(i)


def solve():
    solve_dic = []
    if len(sides) == 2 and len(degs) == 1:
        solve_dic.append("Введи 1 - Вы можете решить по теореме косинусов\n")

    if len(sides) == 1 and len(degs) == 2:
        solve_dic.append("Введи 2 - Вы можете решить по теореме синусов\n")

    if len(sides) == 2 and len(degs) == 0:
        solve_dic.append("Введи 3 - Вы можете решить по теореме Пифагора\n")

    print("Как вы хотите решить задачу?\n"
          "\tДано:")
    for i in range(len(sides)):
        print(f"{i} сторона равна {sides[i]}")
    for i in range(len(degs)):
        print(f"{i} угол равен {degs[i]}")

    user_choise = input("Как вы хотите решить задачу?"
                         "\tДано:"
                         f"Исходя из Ваших данных вот возможные действия"
                         f"{solve_dic}")

    if len(solve_dic) > int(user_choise):
        print("Такой вариант не возможен")
        solve()


def triangle_existence():
    if len(sides) == 3:
        existence = (sides[0] + sides[1]) - sides[2]
        if existence < 0:
            print("Такой треугольник не может существовать!!!")
            main_screen()

"""     if sum(degs) != 180:
        print(f"Сумма градусов введена не верно {sum(degs)}")"""


def a_b_cosj():
    c = math.pow(sides[0], 2) + math.pow(sides[1], 2) - 2 * sides[0] * sides[1] * math.cos(degs[0])
    sides.append(c)
    print("Стороны треуголки равны:\n"
          f"\t A: \t{sides[0]}\n"
          f"\t B: \t{sides[1]}\n"
          f"\t C: \t{sides[2]}\n")
    print(f"\tУгол Альфа равен \t{degs[0]}\n")
