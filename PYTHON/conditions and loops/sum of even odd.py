'''Write a program to input an integer 'n' and print the sum of all its even digits and the sum of all its odd digits separately.Digits mean numbers, not places! That is, if the given integer is "132456", even digits are 2, 4, and 6, and odd digits are 1, 3, and 5.'''
n=int(input())
b=n
e=0
o=0
while b>9:
    c=b%10
    if c%2==0:
        e=e+c
    else:
        o=o+c
    b=b//10
if b%2==0:
    e=e+b
else:
    o=o+b
print(e,"",o)
 
