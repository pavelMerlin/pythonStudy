import random
# notes = ['a', 'ww', 'wqdqwd', 'asd']


def gen_filename():
    names = ["piska.txt", "popa.txt", "govno.txt", "pomoi.txt"]
    gen_name = random.choice(names)
    f = open(gen_name, mode="a")
    f.close()
    print(f"Файл сгенерирован с именем {gen_name}")
    return gen_name


def read_file(file: str):
    with open(file, mode='r', encoding="UTF-8") as f:
        for liner in f.readlines():
            print(liner)


def clear(file: str):
    with open(file, mode='w', encoding="UTF-8") as f:
        f.write("")
        notes_alfa.clear()


def latest():
    notes_alfa.reverse()


def printer():
    for i, note in enumerate(notes_alfa):
        print(f"{i + 1}. {note}")
    print("=" * 5)


def earliest():
    print(notes_alfa)


def longest():
    for j in range(len(notes_alfa)):
        for i in range(len(notes_alfa)):
            note_len = len(notes_alfa[i])
            notes_alfa.append("")
            if note_len < len(notes_alfa[i + 1]):
                notes_alfa[i], notes_alfa[i + 1] = notes_alfa[i + 1], notes_alfa[i]
            notes_alfa.pop(-1)


def shortest():
    longest()
    notes_alfa.reverse()


def add(file):
    add_note = (input(">> "))
    with open(filename, mode='a', encoding="UTF-8") as f:
        f.write(add_note + "\n")
    notes_alfa.append(add_note)
    print("Ты добавил заметку\n")


if __name__ == '__main__':
    notes_alfa = []
    filename = gen_filename()

    print("Ваши предыдущие заметки:\n")
    with open(filename, mode='r', encoding="UTF-8") as f:
        for line in f.readlines():
            print(line)
            notes_alfa.append(line)

    while True:
        user_input = input("Введи команду >> ")

        if user_input == "add":
            add(filename)
            read_file(filename)
        elif user_input == "earliest":
            printer()
        elif user_input == "latest":
            latest()
            printer()
        elif user_input == "save":
            print("Все заметки сохранены")
        elif user_input == "clear":
            clear(filename)
            read_file(filename)
        elif user_input == "longest":
            longest()
            printer()
        elif user_input == "shortest":
            shortest()
            printer()
        elif user_input == "exit":
            quit(0)



