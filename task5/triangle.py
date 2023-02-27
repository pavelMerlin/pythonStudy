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
                if re_input_deg[i] == "":
                    re_input_deg.clear()
                    break
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
    sides.clear()
    degs.clear()

    user_name = random.choice(user_names)
    user_rang = random.choice(user_rangs)

    user_input_side = input(f"\033[37mПривет \033[31m{user_rang} {user_name}\033[37m\n"
                            f"Тут мы считаем возможность существования твоем мамы\n"
                            f"Введи стороны треугольника в формате (сторона A, сторона B или сторона C)\n")

    user_input_deg = input(f"Введи углы треугольника в формате (угол Aльфа, угол Бета или угол Джета(сигма)) "
                           f"или нажми Enter\n")

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
        solve_dic.append("\nВведи 1 - Вы можете решить по теореме косинусов\n")

    if len(sides) == 1 and len(degs) == 2:
        solve_dic.append("\nВведи 2 - Вы можете решить по теореме синусов\n")

    if len(sides) == 2 and len(degs) == 1:
        if degs[0] >= 90:
            solve_dic.append("\nВведи 3 - Вы можете решить по теореме Пифагора\n")

    if len(sides) == 3 and len(degs) == 0:
        solve_dic.append("\nВведи 4 - Вы можете найти периметр\n")
        solve_dic.append("\nВведи 5 - Вы можете найти все углы в треугольнике\n")

    print("Как вы хотите решить задачу?\n"
          "\tДано:")
    for i in range(len(sides)):
        print(f"{i} сторона равна {sides[i]}")
    for i in range(len(degs)):
        print(f"{i} угол равен {degs[i]}")

    print("Как вы хотите решить задачу?\nИсходя из Ваших данных вот возможные действия\n\n")
    for i in solve_dic:
        print(i)

    if len(solve_dic) == 0:
        print("\nС Вашими данными невозможно корректно выполнить ни одну операцию\n")
        main_screen()

    user_choice = input()

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
    else:
        print("\nНевозможно\n")
        main_screen()


if __name__ == '__main__':
    for _ in range(100):
        main_screen()

        triangle_existence()
        solve()



