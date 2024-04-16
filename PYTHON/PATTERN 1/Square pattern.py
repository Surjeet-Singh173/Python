'''Print the following pattern for the given N number of rows.
Pattern for N = 4
4444
4444
4444
4444'''
n=int(input())
a=0
b=0
while a<n:
    while b<n:
        print(n,end="")
        b+=1
    print()
    a+=1
    b=0
