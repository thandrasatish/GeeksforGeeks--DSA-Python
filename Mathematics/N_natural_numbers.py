def Sum_of_N_Natural_Numbers(n):
    return n*(n+1)//2

def Sum_of_N_Natural_Numbers_For_Loop(n):
  total_sum = 0 
  for i in range(1,n+1):
    total_sum += i 
  return total_sum
  

n = int(input())
print(f"Sum_of_N_Natural_Numbers :- {Sum_of_N_Natural_Numbers(n)}")
print(f"Sum_of_N_Natural_Numbers_For_Loop :- {Sum_of_N_Natural_Numbers_For_Loop(n)}")