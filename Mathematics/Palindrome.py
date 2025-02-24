def palindrome(n):
    res = 0 
    temp = n
    while(temp!=0):
        res = res*10 + (temp%10)
        temp = temp//10
    if(n == res):
        return True
    else:
        return False


n = 131
print(f"Palindrome Number or Not : {palindrome(n)}")