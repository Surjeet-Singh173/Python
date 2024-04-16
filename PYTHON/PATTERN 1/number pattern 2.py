'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
202
3003'''
n=int(input())
a=1
while a<=n:
    b=0
    while b<a:
        c=1
        if a==1:
            print(a,end="")
        elif a!=1 and (b==0 or b==a-1) :
            print(a-c,end="")
        else:
            print('0',end="")
        b+=1
    print()
    a+=1