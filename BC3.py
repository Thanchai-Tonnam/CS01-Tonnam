num1 = int(input("num1: "))
num2 = int(input("num2: "))
num3 = int(input("num3: "))
if num1 >= num2 and num1 >= num3:
    mn = num1
elif num2 >= num1 and num2 >= num3:
    mn = num2
else:
    pass

print("max number: ", mn)