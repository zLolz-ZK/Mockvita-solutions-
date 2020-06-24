def countfunc(a):
    if a<=3:
        return 2
    else:
        a=a//2
        return countfunc(a)+1

t=int(input())
for i in range(t):
    n=int(input())
    ans=countfunc(n)
    if n == 1:
        print(1)
    else:
        print(ans)
