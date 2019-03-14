num1 = int(input("Enter first number: "))
highnum = num1
lonum = num1
num2 = int(input("Enter second number: "))
if (num2 > highnum):
    highnum = num2
if (num2 < lonum):
    lonum = num2
num3 = int(input("Enter third number: "))
if (num3 > highnum):
    highnum = num3
if (num3 < lonum):
    lonum = num3
num4 = int(input("Enter fourth number: "))
if (num4 > highnum):
    highnum = num4
if (num4 < lonum):
    lonum = num4
num5 = int(input("Enter fifth number: "))
if (num5 > highnum):
    highnum = num5
if (num5 < lonum):
    lonum = num5

print("highest:", highnum)
print("lowest:", lonum)


