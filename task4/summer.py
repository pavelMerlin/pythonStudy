# num_dict = []
# print("Введи число или sum для суммы")
# while True:
#     result = 0
#     num = input("Введи число: ")
#     try:
#         if num == 'sum':
#             for i in range(len(num_dict)):
#                 result += float(num_dict[i])
#             num_dict.clear()
#         else:
#             float(num)
#             num_dict.append(num)
#         print(result, num_dict)
#     except:
#         print("Фу кака")
#

# вариант 2 ТУТ ЕСТЬ НЕДОРАБОТКИ А ИМЕННО СТРОКА 98 идите нахуй работает не трогай

# словарь символов которые ищем
dictionary = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.']

# количество символов в словаре
col_symbols = len(dictionary)

# массив верно введенных чисел
sum_buffer = []

# главное меню появляется 1 раз
print("\033[37mКалькулятор часть вторая.\n"
      "Вводи числа, а Чтобы выйти из программы напиши \033[31mex\033[37m\n"
      "\t\tВведите \033[31mst\033[37m чтобы просмотреть статус\n"
      "\t\tВведите \033[31mянатурал\033[37m и перейдите в меню помощи\033[0m")

# цикл для постоянного взаимодействия с возможным выходом
while True:
    # ввод числа или команды
    num = input("\033[37mВведи число или команду: \033[0m\t").lower()

    # подходит ли нам введенное число
    num_status = True

    # правда если символ 1 = символу в словаре
    truth = 0

    # если минус не стоит в начале умножаем на 1
    is_minus_first = 1

    # если юзер ввел команду ех
    if num == 'ex':
        quit("Вы завершили программу командой ex")

    # если юзер ввел команду ст
    if num == 'st':
        print(*sum_buffer, end="\t\n")
        continue

    # если длина числа = 0
    if len(num) <= 0:
        print("Неверный ввод с ошибкой 0")
        continue

    # если юзер ввел команду янатурал
    if num == 'янатурал':
        print(f"\n\n\tОшибка 1 - неверный ввод многих символов с буквой\n"
              f"\tОшибка 2 - неверный ввод одного символа с буквой или точки\n"
              f"\tОшибка 3 - неверный ввод  многих символов с буквами и цифрами\n"
              f"\tОшибка 0 - вы ничего не ввели\n")
        num_status = False
        continue

    # если юзер ввел команду сум
    if num == 'sum':
        print(f"\t\n\nСумма: \033[31m{sum(sum_buffer)}\033[0m\n"
              f"\tЧтобы выйти из программы напиши \033[4mex\033[0m\n\n")
        # очищаем массив чисел
        sum_buffer.clear()
        continue

    # если минус стоит вначале меняем переменную на -1 и удаляем его
    if num[0] == '-':
        is_minus_first = -1
        num = num[1:]

    # если юзер ввел только точку
    if len(num) == 1 and num == ".":
        print("Ошибка 2 - неверный ввод одного символа с буквой или точки")
        num_status = False
        continue

    # Узнаем длину введенного пользователем числа
    size_num = len(num)

    # проходимся по всем символам в словаре и сравниваем с числом пользователя
    for i in range(len(dictionary)):

        # Если длина больше одного символа
        if size_num >= 1:

            # проходимся по длине введенного числа
            for j in range(size_num):

                # есть ли совпадение первой цифры числа в словаре
                compare = num[j] is dictionary[i]

                # Если нет выходим и не записываем это число
                if compare is True:
                    truth += 1
                # Если совпадения нет сейчас и переменная равна всем символам словаря и не было ни одного совпадения
                elif compare is False and i == col_symbols - 1 and truth == 0:
                    print("Неверный ввод с ошибкой 1")
                    num_status = False
                    break
        # Если длина числа один символ
        else:
            # Этот символ есть в словаре?
            compare = num in dictionary
            print("aaaaa")
            # Если нет выходим и не записываем это число
            if compare is False:
                print("Неверный ввод с ошибкой 2")
                num_status = False
                break

    # Если количество совпадений меньше символов пример: 3цуц232-12а
    if truth < size_num:
        print("Неверный ввод с ошибкой 3")
        num_status = False

    # добавляем к массиву цифр число пользователя и умножаем на состояние 1 или -1
    if num_status is True:
        sum_buffer.append(float(num) * is_minus_first)
