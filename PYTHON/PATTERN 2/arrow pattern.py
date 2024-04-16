'''Print the following pattern for the given number of rows.
Assume N is always odd.
Note : There is space after every star. Pattern for N = 7
*
 * *
   * * *
     * * * *
   * * *
 * *
*
'''
n=int(input())
a=1
while a<=(n+1)//2:
    b=1
    while b<a:
        print(' ',end="")
        b+=1
    c=1
    while c<=a:
        print('* ',end="")
        c+=1
    print()
    a+=1
a=1
while a<=(n-1)//2:
    b=1
    while b<(n+1)//2-a:
        print(" ",end="")
        b+=1
    c=1
    while c<=(n+1)//2-a:
        print('* ',end="")
        c+=1
    a+=1
    print()
