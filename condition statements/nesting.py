# nesting if statements 

age = int (input("Enter your age: "))

if(age >= 18):
    if(age >= 65):
        print("You are a senior citizen.")
    else:
        print("You are not a senior citizen.")
else:
    print("You are not an adult.")  