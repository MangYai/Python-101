rows = int(input('how many rows?: '))
col = int(input('how many colums?: '))

for i in range(rows):
    for j in range(col):
        print("*", end="")
    print()
