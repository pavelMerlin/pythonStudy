import time
import random

# \033[4m — подчёркнутый;
# \033[37m — белая надпись;
# \033[44m — синий фон;
# {} — заменится на «Python 3»;
# \033[0m — сброс к начальным значениям.
# \033[31m - red

# first bot sentence
anim_printer = "\033[37mПривет я ботик из 1992\033[0m"


# slow bot printer function
def printer(bot_sentence):
    for i in range(len(bot_sentence)):
        print(bot_sentence[i], end="")
        rnd_timeout = random.uniform(.2, .5)
        time.sleep(rnd_timeout)


# print first sentence with function
printer(anim_printer)

# random generator for bot answers
rnd = random.randint(0, 2)


# cycle for questions and answers
while True:
    user_sentence = input("\n\t").lower()

    hello_dictionary = ["привет", "хай", "здравствуй", "добрый "]
    how_are_you = ["как дела", "как движ", "как сам", "что делаешь", "дел"]
    advices = ["посоветуй фильм", "фильм", "посоветуй сериал", "посоветуй"]
    bye_dictionary = ["пока", "до встречи"]

    user_random_names = ["пися", "попа", "кукиш"]
    bot_emotion = ["плохо", "норм", "каифі!"]
    bot_films = ["Сумерки отличный сериал про трах.", "Трансгендер топовый фильм!!!", "рекомендую почитать книгу "
                                                                                      "а не в экран залипать"]

    if user_sentence in hello_dictionary:
        printer(f"\033[37mПривет, {user_random_names[rnd]}, что надо?\033[0m")

    elif user_sentence in how_are_you:
        printer(f"\033[37m{bot_emotion[rnd]}\033[0m")

    elif user_sentence in advices:
        printer(f"\033[37m{bot_films[rnd]}, это сугубо мое мнение {user_random_names[rnd]}\033[0m")

    elif user_sentence in bye_dictionary:
        printer(f"\033[37mНу пока, {user_random_names[rnd]}, до встречи\033[0m")
        quit(0)
    else:
        printer(f"\033[37mПрости, {user_random_names[rnd]}, но я не выкупаю\033[0m")