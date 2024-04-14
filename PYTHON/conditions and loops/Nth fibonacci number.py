'''The n-th term of Fibonacci series F(n), where F(n) is a function, is calculated using the following formula -
    F(n) = F(n - 1) + F(n - 2), 
    Where, F(1) = 1, F(2) = 1
Provided 'n' you have to find out the n-th Fibonacci Number. Handle edges cases like when 'n' = 1 or 'n' = 2 by using conditionals like if else and return what's expected.
"Indexing is start from 1"'''
n=int(input())
a=1
c=3
if n<1:
    print('Invalid input')
elif n==1 or n==2:
    print(a)
else:
    f1=1
    f2=1
    while c<=n:
        f3=f1+f2
        f1=f2
        f2=f3
        c+=1
    print(f3)