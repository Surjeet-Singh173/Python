'''Write a program to generate the reverse of a given number N. Print the corresponding reverse number.
Note : If a number has trailing zeros, then its reverse will not include them. For e.g., reverse of 10400 will be 401 instead of 00401.'''
n=int(input())
b=str(n)
a=len(b)
a=a-1
while a<=0 and n!=0:
    while b[a]=='0':
        b=b[:a-1]
        a=a-1
        if b[a]!='0':
            break
    break
b=int(b)
a=""
while b>9:
    c=int(b%10)
    c=str(c)
    a=a+c
    b=b//10
a=a+str(b)
print(int(a))
