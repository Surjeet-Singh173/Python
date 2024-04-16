'''Print the following pattern for the given N number of rows.
Pattern for N = 3
 A
 BB
 CCC'''
n=int(input())
a=ord('A')
b=1
while b<=n:
    c=1
    while c<=b:
        prt=chr(a+b-1)
        print(prt,end="")
        c+=1
    print()
    b+=1
    