'''Print the following pattern for the given N number of rows.
Pattern for N = 4
*
**
***
****
Note : There are no spaces between the stars (*).'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=a:
        print('*',end="")
        b+=1
    a+=1
    print()
