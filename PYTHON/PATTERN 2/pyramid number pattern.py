'''Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  212
 32123
4321234
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
        print(a+1-c,end="")
        c+=1
    d=1
    while d<a:
        print(d+1,end="")
        d+=1
    print()
    a+=1