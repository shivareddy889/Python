str = "hello world, welcome to python"
new = str[0:5]
print(new)
new1 = str[5:len(str)]
print(new1)
new2 = str[7:]
print(new2)
new3 = str[:6]
print(new3)
new4 = str[:]
print(new4)

#negative indexing starring -1 from the last character
new5 = str[-6:-1]
print(new5) 
new6 = str[-6:]
print(new6) 
new7 = str[-15:]
print(new7)