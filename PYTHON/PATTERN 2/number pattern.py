'''Print the following pattern for n number of rows.
Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
1        1
12      21
123    321
1234  4321
1234554321
'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=a:
        print(b,end="")
        b+=1
    c=1
    while c<=n-a:
        print(" ",end="")
        c+=1
    b=1   
    while b<=n-a:
        print(" ",end="")
        b+=1
    c=1
    while c<=a:
        print(a+1-c,end="")
        c+=1  
    print()
    a+=1
