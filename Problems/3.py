#Given a list of names, print all names that start with the letter 'A'.

list = []

name1 = input("Enter the name:")
name2 = input("Enter the name:")
name3 = input("Enter the name:")
name4 = input("Enter the name:")    
name5 = input("Enter the name:")    
name6 = input("Enter the name:")
list.append(name1)
list.append(name2)
list.append(name3)
list.append(name4)
list.append(name5)
list.append(name6) 
my_list = list.sort()
print("sorted list:",list)
print(type(list))   



or  


names = []

# take 6 names from user
names.append(input("Enter the name:"))
names.append(input("Enter the name:"))
names.append(input("Enter the name:"))
names.append(input("Enter the name:"))
names.append(input("Enter the name:"))
names.append(input("Enter the name:"))

print("Names starting with 'A':")

# check each name manually (no loop, as per your previous preference)
if names[0].startswith('A'):
    print(names[0])
if names[1].startswith('A'):
    print(names[1])
if names[2].startswith('A'):
    print(names[2])
if names[3].startswith('A'):
    print(names[3])
if names[4].startswith('A'):
    print(names[4])
if names[5].startswith('A'):
    print(names[5])