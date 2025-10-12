list = [5, 2, 9, 1, 5, 6]

# sort() method sorts the list in ascending order by default
#mynew = list.sort()

#print("sorted list:", list)

# sort in descending order
newlist2 = list.sort(reverse=True)
print("sorted in descending order:", list)  
print(type(list))

# reverse() method reverses the current order of the list
mylist3 = list.reverse()
print("reversed list:",list)

# insert() method is used to add an element at a specific index
list.insert(2, 15)  # inserting 15 at index 2
print("after insert:", list)

list.insert(0, 20)  # inserting 20 at index 0
print("after insert at index 0:", list)

# remove() method removes the first occurrence of a specified value
list.remove(5)  # removes the first 5
print("after remove:", list)

# pop() method removes and returns the element at the specified index (default is the last element)
popped_element = list.pop()  # removes the last element
print("after pop:", list)
print("popped element:", popped_element)    

popped_element_index = list.pop(0)  # removes element at index 0
print("after pop at index 0:", list)
print("popped element at index 0:", popped_element_index)   
# clear() method removes all elements from the list
list.clear()    
print("after clear:", list)
print(type(list))   

# copy() method creates a shallow copy of the list
list1 = [1, 2, 3, 4, 5]     

list2 = list1.copy()    
print("copied list:", list2)    
