# We add math library
import math


userNum, convertNum = 0, 0
while True:
      # We show txt info in console
      print("Добро пожаловать в перевод градусов!\n"
            "\nВведите \"R\" если вы хотите перевести радианы в градусы"
            "\nВведите \"P\" если вы хотите перевести грудусы в радианы")

      # take user info
      choise = input()

      if choise == 'R':
            userNum = int(input("Введите радианы: "))
            convertNum = math.degrees(userNum)
            break
      elif choise == 'P':
            userNum = int(input("Введите градусы: "))
            convertNum = math.radians(userNum)
            break
      else:
            print("Вы неверно выполнили условия выше!")

print(round(convertNum, 2))