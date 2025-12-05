def char_frequency(s):
    a=list(s)
    for i in range(len(a)):
        
        r=a.count(a[i])
        return dict(b=r,a=r,n=r)
print(char_frequency("banana"))