'''Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
333
22
1
'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=n-a+1:
        print(n-a+1,end="")
        b+=1
    print()
    a+=1