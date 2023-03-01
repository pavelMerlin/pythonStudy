
print("""Меню команд:
`add` - додати нотатку. Користувач вводить текст нотатки, який зберігається у програмі та є дійсним до її завершення
- `earliest` - виводить збережені нотатки у хронологічному порядку - від найранішої до найпізнішої
- `latest` - виводить збережені нотатки у хронологічному порядку - від найпізнішої до найранішої
- `longest` - виводить збережені нотатки у порядку їх довжини - від найдовшої до найкоротшої
- `shortest` - виводить збережені нотатки у порядку їх довжини - від найкоротшоїдо найдовшої\n""")

# notes = ['a', 'ww', 'wqdqwd', 'asd']
notes = []

while True:
    user_input = input("Введи команду >> ")

    if user_input == "add":
        notes.append(input(">> "))
        print("Ты добавил заметку\n")
    elif user_input == "earliest":
        print(notes)
    elif user_input == "latest":
        print(notes.reverse())
    elif user_input == "longest" or user_input == "shortest":
        for j in range(len(notes)):
            for i in range(len(notes)):
                note_len = len(notes[i])
                notes.append("")
                if note_len < len(notes[i + 1]):
                    notes[i], notes[i + 1] = notes[i + 1], notes[i]
                notes.pop(-1)
        if user_input == "sh":
            notes.reverse()

    for i, note in enumerate(notes):
        print(f"{i + 1}. {note}")