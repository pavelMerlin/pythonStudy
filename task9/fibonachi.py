
def fibonache_gen(user_num: int):
    fibonaci_numbers = [1]
    for i in range(0, user_num):
        print(fibonaci_numbers)
        fibonaci_numbers.append(fibonaci_numbers[i - 1] + fibonaci_numbers[i])
    print(fibonaci_numbers)


if __name__ == "__main__":
    user_number = input()
    fibonache_gen(int(user_number))