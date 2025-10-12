 # add set elements
my_set = {"apple", "banana", "cherry"}

my_set.add("orange")
my_set.add("mango")

print(my_set)
print("apple" in my_set)  # True       

# remove set elements
my_set.remove("banana")  # raises KeyError if the element is not found
my_set.discard("grape")  # does not raise an error if the element is not found
my_set.pop()  # removes and returns an arbitrary element from the set
print(my_set)

# update set elements
my_set.update(["kiwi", "watermelon"])  # adds multiple elements to the set
print(my_set)
my_set.update(("grape", "pineapple"))  # adds multiple elements from a tuple
print(my_set)

# clear set elements
my_set.clear()  # removes all elements from the set
print(my_set)  # prints an empty set
print(len(my_set))  # prints the number of elements in the set
print(type(my_set))  # prints the type of the set
print(len(my_set))

#removed = my_set.pop()  # removes and returns an arbitrary element from the set
#print(removed)  # prints the removed element
#print(len(my_set))  # prints the set after removing the element
#print(my_set)

# union, intersection, difference, symmetric difference
# union

set1 = {"apple", "banana", "cherry"}
set2 = {"cherry", "date", "fig"}
print(set1.union(set2))  # {'apple', 'banana', 'cherry', 'date', 'fig'}
print(set1 | set2)  # {'apple', 'banana', 'cherry', 'date', 'fig'}

# intersection
print(set1.intersection(set2))  # {'cherry'}
print(set1 & set2)  # {'cherry'}
# difference
print(set1.difference(set2))  # {'apple', 'banana'}
print(set1 - set2)  # {'apple', 'banana'}
# symmetric difference
print(set1.symmetric_difference(set2))  # {'apple', 'banana', 'date', 'fig'}
print(set1 ^ set2)  # {'apple', 'banana', 'date', 'fig'}
# subset, superset, disjoint
set3 = {"apple", "banana"}
print(set3.issubset(set1))  # True
print(set1.issuperset(set3))  # True        
print(set1.isdisjoint(set2))  # False

print(set1)
print(set2)
print(set3)

active_servers = {"server1", "server2", "server3"}
failed_servere = {"server2", "server4"}

healthy = active_servers.difference(failed_servere)
print("healthy servers:", healthy)


