fnum = int(input('Enter the first number:'))
snum = int(input ('Enter the second number:'))

op = input('Enter the operation:')
if op == "+":
    print(fnum + snum)
elif op == "-":
    print( fnum - snum)
elif op == "*":
    print(fnum * snum)
else:
    print(fnum / snum)