'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1234
123
12
1'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=n-a+1:
        print(b,end='')
        b+=1
    print()
    a=a+1
