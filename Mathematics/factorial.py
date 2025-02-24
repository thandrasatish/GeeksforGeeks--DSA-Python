def factorial(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i 
    return fact 

n = int(input())
print(f"factorial of a number {n} : {factorial(n)}")

def rec_factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)

n = int(input())
print(f"factorial of a recersive number {n} : {rec_factorial(n)}")