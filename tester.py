
input_palindrome = "A >B"

ban_symbols = ['>', '.', ',', '-', ':', ';', '?', '!', '"', "'", " "]
#
# for  i in range(len(ban_symbols)):
user = input_palindrome
for i in range(len(ban_symbols)):
    user = input_palindrome.lower().replace(ban_symbols[i], "")
# user_palindrome = input_palindrome.lower().replace(ban_symbols[0], "")
print(f"{user}")