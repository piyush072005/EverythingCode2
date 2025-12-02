n=input("enter number")
for i in n:
    r=int(n)%10
    print(r,end="")
    n=int(n)//10