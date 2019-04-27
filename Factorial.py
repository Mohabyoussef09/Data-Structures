def factorialRecursion(n):
    if n==1:
        return 1
    
    return n*factorialRecursion(n-1)

factorialRecursion(5)

def factorialIterative(n):
    fact=n
    while n>1:
        n-=1
        fact*=n
    return fact
factorialIterative(5)

