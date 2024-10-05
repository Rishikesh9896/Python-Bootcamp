num1 = int(input("Enter the first number"))
num2 = int(input("Enter the second number"))
num3 = int(input("Enter the third number"))
if(num1>num2 and num1>num3):
    print("The first number is greatest")
elif(num2>num3 and num2>num1):
    print("The second number is greatest")
else:
    print("The third number is greatest")
    