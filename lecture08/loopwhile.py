with open("example.txt", "r") as file:
    line = file.readline()
    while line:
        print(line.strip())     # strip() removes \n
        line = file.readline()