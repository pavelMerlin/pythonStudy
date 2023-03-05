with open("weed.txt") as f:
    output = ["" if line.find("a") == -1 else line.strip()[line.find("a"):].capitalize() for line in f.readlines()]
    print(output)