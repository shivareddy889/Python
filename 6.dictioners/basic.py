# dictionaries are mutable, unordered collections of key-value pairs
# keys must be unique and immutable (strings, numbers, tuples)
# mutable types (lists, dictionaries) cannot be used as keys
# values can be of any data type and can be duplicated
# mutable mean you can change, add, remove items after the dictionary has been created
# immutable mean you cannot change, add, remove items after the tuple has been created  

dict1 = {
    "name" : "shiva",
    "age" : 25,
    "city" : "hyd",
    "frnds" : ["ram", "laxman", "sita"]
}

print(dict1)
print(dict1.get("age"))

print(dict1["name"])

# Accessing Values

#["key"] — directly fetches value (error if key not found)
# .get("key") — safely fetches value (no error if key missing)

# adding new key-value pair
dict1["location"] = "India"
print(dict1)

# updating existing key-value pair
dict1["age"] = 26   
print(dict1)

# removing key-value pair
del dict1["city"]       
print(dict1)    

del dict1["frnds"]
print(dict1)

dict1["place"] = "mumbai"
print(dict1)

# diff between pop and del
# pop returns the value of the removed key, del does not return anything
# pop is a method, del is a statement
# pop can be used on lists too, del cannot be used on lists
# pop can take a default value if key not found, del cannot
# pop raises KeyError if key not found, del raises KeyError if key not found
# pop is more flexible, del is more straightforward
# pop is used when you want to use the removed value, del is used when you just want to remove the key-value pair
# pop is a method of dictionary, del is a built-in statement in python
# popitem removes and returns the last inserted key-value pair as a tuple
# popitem is useful for implementing LIFO (last-in, first-out) data structures like stacks, while del is used for general key-value pair removal

dict1.popitem()
print(dict1)    
