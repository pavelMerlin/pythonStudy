

def read_file(file: str):
    with open(file, mode="r") as f:
        text_lines = [line.strip() for line in f.readlines()]
        find_letter(text_lines)


def find_letter(text_lines: list):
    print(text_lines, type(text_lines))
    for i in range(len(text_lines)):
        if text_lines[i].find("a") == -1:
            text_lines[i] = ""
        else:
            index_a = text_lines[i].find("a")
            text_lines[i] = text_lines[i][index_a:]
        text_lines[i] = text_lines[i].capitalize()
    print(text_lines)


if __name__ == "__main__":
    read_file("weed.txt")


