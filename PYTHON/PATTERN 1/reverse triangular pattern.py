'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1
21
321
4321'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=a:
        print(a+1-b,end='')
        b=b+1
    a=a+1
    print()