def is_Prime(n):
    if n <= 1:
        return False 
    if(n==2 or n ==3):
        return True
    
    if(n%2 ==0 or n%3 ==0):
        return False 
    

    i = 5
    while(i*i<=n):
        if(n%i ==0 or n%(i+2)==0):
            return False
        i += 6
    return True


def prime_factors_of_N(n):
    for i in range(2,n+1):
        if(is_Prime(i)):
            while(n%i==0):
                print(i,end= " ")
                n //=i 


n = 100
prime_factors_of_N(n)

