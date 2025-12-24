def love():
    answer = input("Do You Love Me? (yes/no): ")

    if answer.lower() == "yes":
        print("I Love You")
    else:
        love()

love()