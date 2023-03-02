import random
import math
import time
from data import *
from triangle import *


def triangle_existence():
    if len(sides) == 3:
        existence = (sides[0] + sides[1]) - sides[2]
        if existence <= 0:
            print("\033[31mТакой треугольник не может существовать!!!\n")
            main_screen()

    if len(degs) == 3:
        info = sum(degs) != 180
        if info is True:
            print(f"\033[31mСумма градусов введена не верно {sum(degs)}\n")
            main_screen()

    if len(sides) > 3 or len(degs) > 3:
        print("\033[31mОшибка ввода\n")
        main_screen()
    elif len(sides) == 0:
        print("\033[31mОшибка ввода\n")
        main_screen()
    elif len(sides) == 1 and len(degs) < 0:
        print("\033[31mОшибка ввода\n")
        main_screen()


def a_sina_sinb():
    degs.append(abs(degs[0] + degs[1] - 180))

    a = sides[0] * math.sin(math.radians(degs[0])) / math.sin(math.radians(degs[2]))

    b = sides[0] * math.sin(math.radians(degs[1])) / math.sin(math.radians(degs[2]))

    c = sides[0]

    print("Стороны треуголки равны:\n"
          f"\t A: \t{round(a, 2)}\n"
          f"\t B: \t{round(b, 2)}\n"
          f"\t C: \t{round(c, 2)}\n")
    print(f"\tУгол Альфа равен \t{degs[2]}\n")
    sides[0] = a
    sides.append(b)
    sides.append(c)
    time.sleep(2)


def deg_find():
    cos_a = (sides[0] ** 2 + sides[2] ** 2 - sides[1] ** 2) / (2 * sides[0] * sides[2])

    cos_b = (sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) / (2 * sides[0] * sides[1])

    cos_c = (sides[1] ** 2 + sides[2] ** 2 - sides[0] ** 2) / (2 * sides[2] * sides[1])

    print(f"{degs.append(round(math.degrees(math.acos(cos_a))), 2)} угол А\n"
          f"{degs.append(round(math.degrees(math.acos(cos_b))), 2)} угол B\n"
          f"{degs.append(round(math.degrees(math.acos(cos_c))), 2)} угол J\n")
    time.sleep(2)


def a_b_cosj():
    c = math.sqrt(pow(sides[0], 2) + pow(sides[1], 2) - 2 * sides[0] * sides[1] * math.cos(math.radians(degs[0])))

    sides.append(round(c, 2))
    print("Стороны треуголки равны:\n"
          f"\t A: \t{sides[0]}\n"
          f"\t B: \t{sides[1]}\n"
          f"\t\033[37mC: \t{sides[2]}\033[0m\n")
    print(f"\tУгол Альфа равен \t{degs[0]}\n")
    time.sleep(2)


def perimetr():
    p = sides[0] + sides[1] + sides[2]
    print(p)
    time.sleep(2)


def height():
    p = (sides[0] + sides[1] + sides[2]) / 2
    h.append((2 * math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))) / sides[0])
    print(f"Высота равна: {round(*h, 2)}\n")
    time.sleep(2)


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
    time.sleep(2)
