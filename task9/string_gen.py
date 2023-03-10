
def string_reader(user_string: str):
    final_input = user_string.split(" ")
    print(*[final_input[i] + "\n" for i in range(len(final_input))], end="")


if __name__ == "__main__":
    user_input = input()
    string_reader(user_input)


