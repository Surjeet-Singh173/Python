# find x raise to the power n where x is a float and n is integer In the output, you will see the number returned by you upto 6 decimal places.
x=float(input())
n=int(input())
power=x**n
print("{:.6f}".format(power))