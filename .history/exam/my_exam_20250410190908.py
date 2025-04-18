def  f(n):
    if n==0:
        return 0
    else:
        return 1 + f(n&(n-1))
print(f(15))
