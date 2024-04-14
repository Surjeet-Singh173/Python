'''Problem statement
Check whether a given number ’n’ is a palindrome number.
Note :
Palindrome numbers are the numbers that don't change when reversed.
You don’t need to print anything. Just implement the given function.
Example:
Input: 'n' = 51415
Output: true
Explanation: On reversing, 51415 gives 51415.'''
n=int(input())
b=n
c=""
while b>9:
    d=b%10
    c=c+str(d)
    b=b//10
c=str(b)
c=int(c)
flag=True
if c!=n:
    flag=False
if flag:
    print("true")
else:
    print("false")