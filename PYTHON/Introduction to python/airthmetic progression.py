#You are given first three entries of an arithmetic progression. You have to calculate the common difference and print it.
a=int(input());
b=int(input());
c=int(input());
c_d1=b-a
c_d2=c-b
if(c_d1==c_d2):
    print(c_d1);
