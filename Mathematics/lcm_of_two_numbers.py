def optimize_gcd_of_two_numbers(a,b):
    if(b == 0):
        return a 
    return optimize_gcd_of_two_numbers(b,a%b)

def lcm_of_two_numbers(a,b):

    return a*b//optimize_gcd_of_two_numbers(a,b)


a = int(input())
b = int(input())

print(lcm_of_two_numbers(a,b))