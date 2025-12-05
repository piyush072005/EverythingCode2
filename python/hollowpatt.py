rows = 5
cols = 10

for i in range(rows):
    if i == 0:
        print("*")
    elif i == rows - 1:
        print("*" * cols)
    else:
        print("" + " " * i + "")"*" + (" " * (cols - 2) + "*")
    print("")