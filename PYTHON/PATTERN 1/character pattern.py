'''Print the following pattern for the given N number of rows.
Pattern for N = 4
A
BC
CDE
DEFG'''
n=int(input())
a=ord('A')
b=1
while b<=n:
    c=1
    str=a+b-1
    while c<=b:
        prt=chr(str+c-1)
        print(prt,end="")
        c+=1
    b+=1
    print()
