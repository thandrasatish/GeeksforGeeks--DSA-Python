def count_of_digits(n):
    c=0
    while(n>0):
        c=c+1
        n=n//10
    return c
n = 1901
print(f"count of digits: {count_of_digits(n)}")