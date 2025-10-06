numbers = []

# taking 4 numbers from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

# adding them into the list
numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)

print("Even numbers are:")

# check each one manually (without loop)
if num1 % 2 == 0:
    print(num1)
if num2 % 2 == 0:
    print(num2)
if num3 % 2 == 0:
    print(num3)
if num4 % 2 == 0:
    print(num4)