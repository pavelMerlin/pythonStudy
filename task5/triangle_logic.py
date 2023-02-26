import random
import math
from data import *
from triangle import *


def triangle_existence():
    if len(sides) == 3:
        existence = (sides[0] + sides[1]) - sides[2]
        if existence < 0:
            print("Такой треугольник не может существовать!!!")
            main_screen()


def a_sina_sinb():
    degs.append(abs(degs[0] + degs[1] - 180))

    a = sides[0] * math.sin(math.radians(degs[0])) / math.sin(math.radians(degs[2]))

    b = sides[0] * math.sin(math.radians(degs[1])) / math.sin(math.radians(degs[2]))

    print("Стороны треуголки равны:\n"
          f"\t A: \t{a}\n"
          f"\t B: \t{b}\n"
          f"\t C: \t{sides[0]}\n")
    print(f"\tУгол Альфа равен \t{degs[2]}\n")


def a_b_cosj():
    c = math.sqrt(pow(sides[0], 2) + pow(sides[1], 2) - 2 * sides[0] * sides[1] * math.cos(math.radians(degs[0])))
    sides.append(round(c, 2))
    print("Стороны треуголки равны:\n"
          f"\t A: \t{sides[0]}\n"
          f"\t B: \t{sides[1]}\n"
          f"\t C: \t{sides[2]}\n")
    print(f"\tУгол Альфа равен \t{degs[0]}\n")


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

