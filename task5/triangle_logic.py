import random
from data import *


# реюзаюильность / 100+ строк / класс

def main_screen():
    user_name = random.choice(user_names)
    user_rang = random.choice(user_rangs)

    user_input = input(f"\033[37mПривет \033[31m{user_rang} {user_name}\033[37m\n"
                       f"Тут мы считаем возможность существования твоем мамы\n"
                       f"Введи стороны треугольник в формате (сторона а, сторона b или сторона c)\n")

    re_input = user_input.split(" ")
    print(re_input)
    try:
        for i in range(len(re_input)):
            detect_word = "сторона" in re_input
            # float(re_input[i])
            print(detect_word)
    except:
        print("Вы ввели значение стороны некорректно")
