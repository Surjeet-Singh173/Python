'''Print the following pattern
Pattern for N = 4
   *
  ***
 *****
*******
'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=n-a:
        print(' ',end="")
        b+=1
    c=1
    while c<=a:
        print('*',end='')
        c+=1
    c=a
    while c>1:
        print('*',end='')
        c-=1
    print()
    a+=1