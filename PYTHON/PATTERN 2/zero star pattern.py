'''Print the following pattern
Pattern for N = 4
*000*000*
0*00*00*0
00*0*0*00
000***000'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=n:
        if b==a:
            print('*',end="")
            b+=1
        else:
            print('0',end="")
            b+=1
    print('*',end="")
    b=1
    while b<=n:
        if b==(n-a+1):
            print('*',end="")
            b+=1
        else:
            print('0',end="")
            b+=1
    print()
    a+=1