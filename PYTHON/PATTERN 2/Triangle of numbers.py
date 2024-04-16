'''Print the following pattern for the given number of rows.
Pattern for N = 4
   1
  232
 34543
4567654
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
        print(a+c-1,end="")
        c+=1
    d=c-1
    c=a-1
    while c>=1:
        print(d+c-1,end="")
        c-=1
    print()
    a+=1