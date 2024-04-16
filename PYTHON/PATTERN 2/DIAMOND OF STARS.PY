'''Print the following pattern for the given number of rows.
Note: N is always odd.
Pattern for N = 5
  *
 ***
*****
 ***
  *
'''
n=int(input())
a=1
while a<=(n+1)//2:
  b=1
  while b<=(n+1)//2-a:
    print(' ',end="")
    b+=1
  c=1
  while c<=a:
    print('*',end='')
    c+=1
  d=1
  while d<a:
    print('*',end="")
    d+=1
  print()
  a+=1
a=1
while a<=(n-1)//2:
  b=1
  while b<=a:
    print(' ',end="")
    b+=1
  c=1
  while c<=(n-1)//2-a+1:
    print('*',end="")
    c+=1
  d=1
  while d<=(n-1)//2-a:
    print('*',end="")
    d+=1
  a+=1
  print()
