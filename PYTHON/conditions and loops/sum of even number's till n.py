'''Given a number N, print sum of all even numbers from 1 to N.'''
N=int(input())
count=2
output=0
while count<=N:
    output=output+count
    count=count+2
print(output)