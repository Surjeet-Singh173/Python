'''Print the following pattern for the given N number of rows.
Pattern for N = 4
1
11
111
1111'''
n=int(input())
a=1
while a<=n:
    b=1
    while b<=a:
        print('1',end="")
        b+=1
    a+=1
    print()

