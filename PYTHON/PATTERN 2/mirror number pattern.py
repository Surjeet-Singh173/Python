'''Print the following pattern for the given N number of rows.
Pattern for N = 4
   1
  12
 123
1234
The dots represent spaces.'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=n-a:
        print(' ',end="")
        b+=1
    c=1
    while c<=a:
        print(c,end='')
        c+=1
    print()
    a+=1
