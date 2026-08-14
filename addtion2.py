number = int(input("Enter three digit number:"))
# 345%10->5
a=number%10
number=number//10
# 34%10 -> 4
b=number%10
number=number//10
# 3%10 -> 3
c=number%10
print(a + b + c)