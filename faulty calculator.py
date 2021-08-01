print("enter 1st number")
num1 = int(input())
print("enter 2nd number")
num2 = int(input())
print("what you want to print? ")
num3 = input()
if num1 ==45 and num2 ==3 and num3 =='+':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
    print("77")
elif num1 == 56 and num2 == 6 and num3 == '/' :
    print("4")
elif num3 == '*':
    num4 =num1*num2
    print(num4)
elif num3 == '+':
    num4 = num1 + num2
    print(num4)
elif num3 == '-':
    num4 = num1 - num2
    print(num4)
elif num3 == '/':
    num4 = num1 / num2
    print(num4)
else: print('out of range')