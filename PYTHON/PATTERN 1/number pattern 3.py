'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
121
1221'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=a:
        if b==1 or b==a:
            print('1',end="")
        else:
            print('2',end="")
        b+=1
    print()
    a+=1   