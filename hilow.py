print("Do numbers (0 min, 10000 max)")
num1 = int(input("Do first number: "))
while (num1 < 0 or num1 > 10000):
    num1 = int(input("You didn't do! Do first number: "))
def print_results(highest, lowest):
    print("highest:", highest)
    print("lowest:", lowest)
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
num6 = int(input("Enter sixth number: "))
while (num6 < 0 or num6 > 10000):
    num6 = int(input("You didnt't do! Do sixth number: "))
if (num6 > highnum):
    highnum = num6
if (num6 < lonum):
    lonum = num6
num7 = int(input("Enter seventh number: "))
while (num7 < 0 or num7 > 10000):
    num7 = int(input("You didnt't do! Do seventh number: "))
if (num7 > highnum):
    highnum = num7
if (num7 < lonum):
    lonum = num7
num8 = int(input("Enter eighth number: "))
while (num8 < 0 or num8 > 10000):
    num8 = int(input("You didnt't do! Do eighth number: "))
if (num8 > highnum):
    highnum = num8
if (num8 < lonum):
    lonum = num8
num9 = int(input("Enter ninth number: "))
while (num9 < 0 or num9 > 10000):
    num9 = int(input("You didnt't do! Do ninth number: "))
if (num9 > highnum):
    highnum = num9
if (num9 < lonum):
    lonum = num9
num10 = int(input("Enter tenth number: "))
while (num10 < 0 or num10 > 10000):
    num10 = int(input("You didnt't do! Do tenth number: "))
if (num10 > highnum):
    highnum = num10
if (num10 < lonum):
    lonum = num10

print_results(highnum, lonum)



