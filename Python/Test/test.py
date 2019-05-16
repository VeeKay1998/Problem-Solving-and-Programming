def fa(n):
    f=1
    while n>1:
        f=f*n
        n=n-1
    return f    


def pr(n):
    for count in range (0,n):
        print(n[count])
        