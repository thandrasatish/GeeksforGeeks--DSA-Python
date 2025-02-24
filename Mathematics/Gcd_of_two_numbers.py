def gcd_of_two_numbers(a,b):
    while(b!=0):
        a,b = b,a%b
    return a

def optimize_gcd_of_two_numbers(a,b):
    if(b == 0):
        return a 
    return optimize_gcd_of_two_numbers(b,a%b)


a = int(input())
b = int(input())
print(f"GCD of Two Numbers : {gcd_of_two_numbers(a,b)}")
print(f"GCD of Two Numbers : {optimize_gcd_of_two_numbers(a,b)}")