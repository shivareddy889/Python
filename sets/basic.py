# set 
# A set is an unordered collection of unique elements.  
# Sets are mutable, meaning you can add or remove elements after creation.
# Sets do not allow duplicate elements. If you try to add a duplicate, it will be
# ignored.
# Sets are defined using curly braces {} or the set() function.
# Sets are useful for membership testing, removing duplicates from a list, and performing mathematical set operations like union, intersection, and difference.
# Sets are unordered, meaning the elements do not have a defined order and cannot be accessed by index.
# Sets can contain elements of different data types, including numbers, strings, and tuples (but not lists or dictionaries, as they are mutable).
# Example of creating a set

my_set = {"apple", "banana", "cherry"}
print(my_set)
print(type(my_set))

# duplicate elements will be ignored
my_set = {"apple", "banana", "cherry", "apple", "banana"}
print(my_set)   

empty_set = set()  # correct way to create an empty set
print(type(empty_set))

# empty_set = {}  # this creates an empty dictionary, not a set
# print(type(empty_set))

# Adding elements to a set
my_set.add("orange")
print(my_set)
my_set.add("mango")

print("apple" in my_set)  # True
print("grape" in my_set)  # False