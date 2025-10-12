# WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)

list1 = [121, 131, 20, 30, 141, 151]
list2 = list1.copy()    
list2.reverse()     
if(list1 == list2):
    print("list contains palindrome elements")      
else:
    print("list does not contain palindrome elements")  
print("original list:",list1)
print("reversed list:",list2)   