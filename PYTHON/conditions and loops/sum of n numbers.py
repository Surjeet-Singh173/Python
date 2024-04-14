'''Given an integer n, find and print the sum of numbers from 1 to n.

Note
Use while loop only.'''
n=int(input())
total=0
count=1
while (count<=n):
    total=total+count
    count=count+1
print(total)