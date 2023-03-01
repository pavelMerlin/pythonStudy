import random
import math
from data import *
from triangle import *


def triangle_existence():
    if len(sides) == 3:
        existence = (sides[0] + sides[1]) - sides[2]
        if existence <= 0:
            print("Такой треугольник не может существовать!!!\n")
            main_screen()

    if len(degs) == 3:
        info = sum(degs) != 180
        if info is True:
            print(f"Сумма градусов введена не верно {sum(degs)}\n")
            main_screen()

    if len(sides) > 3 or len(degs) > 3:
        print("Ошибка ввода")
        main_screen()
    elif len(sides) == 0:
        print("Ошибка ввода")
        main_screen()
    elif len(sides) == 1 and len(degs) < 0:
        print("Ошибка ввода")
        main_screen()


def a_sina_sinb():
    degs.append(abs(degs[0] + degs[1] - 180))

    a = sides[0] * math.sin(math.radians(degs[0])) / math.sin(math.radians(degs[2]))

    b = sides[0] * math.sin(math.radians(degs[1])) / math.sin(math.radians(degs[2]))

    print("Стороны треуголки равны:\n"
          f"\t A: \t{round(a, 2)}\n"
          f"\t B: \t{round(b, 2)}\n"
          f"\t C: \t{sides[0]}\n")
    print(f"\tУгол Альфа равен \t{degs[2]}\n")


def deg_find():
    cos_a = (sides[0] ** 2 + sides[2] ** 2 - sides[1] ** 2) / (2 * sides[0] * sides[2])

    cos_b = (sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) / (2 * sides[0] * sides[1])

    cos_c = (sides[1] ** 2 + sides[2] ** 2 - sides[0] ** 2) / (2 * sides[2] * sides[1])

    print(f"{round(math.degrees(math.acos(cos_a)), 2)} угол А\n"
          f"{round(math.degrees(math.acos(cos_b)), 2)} угол B\n"
          f"{round(math.degrees(math.acos(cos_c)), 2)} угол J\n")


def a_b_cosj():
    c = math.sqrt(pow(sides[0], 2) + pow(sides[1], 2) - 2 * sides[0] * sides[1] * math.cos(math.radians(degs[0])))
    sides.append(round(c, 2))
    print("Стороны треуголки равны:\n"
          f"\t A: \t{sides[0]}\n"
          f"\t B: \t{sides[1]}\n"
          f"\t C: \t{sides[2]}\n")
    print(f"\tУгол Альфа равен \t{degs[0]}\n")


def perimetr():
    p = sides[0] + sides[1] + sides[2]
    print(p)


def height():
    p = (sides[0] + sides[1] + sides[2]) / 2
    h = (2 * math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))) / sides[0]
    print(f"Высота равна: {round(h, 2)}\n")


def pifagor():

    user_choise = input("Вы ищете гипотенузу? + / -\n")

    if user_choise == "+":
        c = math.sqrt(pow(sides[0], 2) + pow(sides[1], 2))
        print(round(c, 2))
    elif user_choise == "-":
        if sides[0] >= sides[1]:
            c = math.sqrt(pow(sides[0], 2) - pow(sides[1], 2))
        else:
            c = math.sqrt(pow(sides[1], 2) - pow(sides[0], 2))
        print(round(c, 2))
    else:
        print("Вы ввели опцию некорректно")
        main_screen()

