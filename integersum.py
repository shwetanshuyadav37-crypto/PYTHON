n = int(input("Enter N: "))
i = 1
sum = 0
while i <= n:
    if i % 5 == 0:
        i = i + 1
        continue
    sum = sum + i
    if sum > 300:
        break
    i = i + 1
print("Final sum:",sum)
