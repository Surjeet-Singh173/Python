'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1
22
333
4444'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=a:
        print(a,end="")
        b+=1
    a+=1
    print()

    
    