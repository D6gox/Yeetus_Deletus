print("Do numbers (0 min, 10000 max)")
num1 = int(input("Do first number: "))
while (num1 < 0 or num1 > 10000):
    num1 = int(input("You didn't do! Do first number: "))
highnum = num1
lonum = num1
num2 = int(input("Do second number: "))
while (num2 < 0 or num2 > 10000):
    num2 = int(input("You didn't do! Do second number: "))
if (num2 > highnum):
    highnum = num2
if (num2 < lonum):
    lonum = num2
num3 = int(input("Do third number: "))
while (num3 < 0 or num3 > 10000):
    num3 = int(input("You didn't do! Do third number: "))
if (num3 > highnum):
    highnum = num3
if (num3 < lonum):
    lonum = num3
num4 = int(input("Do fourth number: "))
while (num4 < 0 or num4 > 10000):
    num4 = int(input("You didn't do! Do fourth number: "))
if (num4 > highnum):
    highnum = num4
if (num4 < lonum):
    lonum = num4
num5 = int(input("Do fifth number: "))
while (num5 < 0 or num5 > 10000):
    num5 = int(input("You didnt't do! Do fifth number: "))
if (num5 > highnum):
    highnum = num5
if (num5 < lonum):
    lonum = num5

print("highest:", highnum)
print("lowest:", lonum)


