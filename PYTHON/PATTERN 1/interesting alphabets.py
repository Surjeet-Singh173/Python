'''Print the following pattern for the given number of rows.
Pattern for N = 5
E
DE
CDE
BCDE
ABCDE'''
n=int(input())
a=ord('A')
b=1
while b<=n:
    c=1
    while c<=b:
        str=chr(a+n-b+c-1)
        print(str,end="")
        c+=1
    b+=1
    print()
