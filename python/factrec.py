n=int(input("enter number"))
def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)
if n<0:
    print("you cant find negative no. factorial")
elif n==0:
    print("0 factorial is 1")
else:
    result=fact(n)
print(result)