# take user info
user_string = input("Введи строку балбес\n"
                    ">>> ")

# find brackets
open_bracket = user_string.find('(')
close_bracket = user_string.find(')')

# find symbols between brackets
between_symbols = user_string[open_bracket:close_bracket + 1]

# delete symbols between brackets
user_string = user_string.replace(between_symbols, "")
print(user_string)

# Example: aaaaa (rrr) bbbbb(aaa)f
