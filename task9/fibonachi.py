def fibonacci_gen(user_num: int):
    fibonacci_numbers = [0, 1]
    for i in range(2, user_num):
        fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])
    return fibonacci_numbers


if __name__ == "__main__":
    user_number = int(input())
    print(fibonacci_gen(user_number))