# WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number: "))
if(num % 2 == 0):
    print(num, "is an even number.")
else:
    print(num, "is an odd number.") 


# WAP to find the greatest of 3 numbers entered by the user.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if(num1>=num2 and num1>=num3):
    print(num1, "is the greatest number.")
elif(num2>=num1 and num2>=num3):
    print(num2, "is the greatest number.")
else:
    print(num3, "is the greatest number.")

# WAP to check if a number entered by the user is a multiple of 7 or not.

number = int(input("Enter a number: "))
if(number %7 == 0):
    print(number, "is a multiple of 7.")
else:
    print(number, "is not a multiple of 7.")