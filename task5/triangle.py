import random
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

    re_input_side = []
    re_input_deg = []

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
    if len(re_input_deg) == 3:
        info = sum(degs) != 180
        if info is True:
            print(f"Сумма градусов введена не верно {sum(degs)}")
            main_screen()
    if len(re_input_side) == 3:
        triangle_existence()

    detect_words(re_input_side, re_input_deg)

    for i in re_input_side:
        sides.append(i)
    for i in re_input_deg:
        degs.append(i)


def solve():
    solve_dic = []
    if len(sides) == 2 and len(degs) == 1:
        solve_dic.append("\nВведи 1 - Вы можете решить по теореме косинусов\n")

    if len(sides) == 1 and len(degs) == 2:
        solve_dic.append("\nВведи 2 - Вы можете решить по теореме синусов\n")

    if len(sides) == 2 and degs[0] == 90:
        solve_dic.append("\nВведи 3 - Вы можете решить по теореме Пифагора\n")

    print("Как вы хотите решить задачу?\n"
          "\tДано:")
    for i in range(len(sides)):
        print(f"{i} сторона равна {sides[i]}")
    for i in range(len(degs)):
        print(f"{i} угол равен {degs[i]}")

    print("Как вы хотите решить задачу?\nИсходя из Ваших данных вот возможные действия\n\n")
    for i in solve_dic:
        print(i)

    user_choice = input()

    if user_choice == '1':
        a_b_cosj()
    elif user_choice == '2':
        a_sina_sinb()
    elif user_choice == '3':
        pifagor()
    else:
        print("\nНевозможно\n")
        main_screen()


if __name__ == '__main__':
    for _ in range(100):
        main_screen()

        solve()
        triangle_existence()


