# Trailing Zeros in Factorial 

def find_trailing_zeros(n):
    if(n<0):
        return -1 
    
    count = 0 

    i = 5
    while((n//i) >= 1):
        count += (n//i)
        i *= 5
    
    return count 


n = 100
print(find_trailing_zeros(n))