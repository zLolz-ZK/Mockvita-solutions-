#worked for 2nd example test case not 1st also i got tle 
from itertools import permutations
def isprime(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0: return 0
        else: return 1      
    else: return 0
    
def fibo(a,b,n):
    if n == 1: return a
    elif n == 2: return b 
    else: return fibo(a,b,n-1)+fibo(a,b,n-2)
    
n1,n2= map(int,input().split())
#gen list from n1 & n2
lst=[str(i) for i in range(n1,n2+1) if isprime(i) == 1]
per_lst = list(permutations(lst,2))
prime_lst = [int(i[0]+i[1]) for i in per_lst if isprime(int(i[0]+i[1])) == 1]

length=len(prime_lst)
a=min(prime_lst)
b=max(prime_lst)
print(fibo(a,b,length),a,b,length)
