'''Given three values - Start Fahrenheit Value (S), End Fahrenheit value (E) and Step Size (W), you need to convert all Fahrenheit values from Start to End at the gap of W, into their corresponding Celsius values and print the table.'''
fs=int(input())
fe=int(input())
w=int(input())
while fs<=fe:
    c=int((fs-32)*5/9)
    print(fs," ",c)
    fs=fs+w
