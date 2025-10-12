#indexing

t = (10,20,30,40,50,60,70,80,90)
my_tup = t.index(40)  #index(value,start,end)
print("index of 40 is:",my_tup)

my_tup1 = t.index(70)
print("index of 70 is:",my_tup1)    

# counting the number of occurrences of a value in a tuple
my_tup2 = t.count(20)
print("count of 20 is:",my_tup2)

trr = (1,2,3,2,4,5,2,6,2)
my_tup3 = trr.count(2)
print("count of 2 is:",my_tup3) 


#slicing
tup = (10,20,30,40,50,60,70,80,90)
newtup = tup[2:7]  #slicing from index 2 to index 6 (7-1)   

print(newtup)
newtup1 = tup[3:6]
print(newtup1)          
newtup2 = tup[4:]
print(newtup2)  
newtup3 = tup[5:len(tup)]