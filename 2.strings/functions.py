str = "hello world, welcome to python"

# string functions

upper = str.upper()       # converts to uppercase
lower = str.lower()       # converts to lowercase
print("all are upper",upper)
print("all are lower",lower)


#capitalize

text = str.capitalize()  # capitalizes the first letter
print("capitalize the first letter",text)

# endwith

ends = str.endswith("python")  # checks if string ends with a specific substring
print("string ends with python",ends)
not_ends = str.endswith("java")  # checks if string ends with a specific substring
print("string not ends with java",not_ends)


# startswith
starts = str.startswith("hello")  # checks if string starts with a specific substring
print("string starts with hello",starts)
not_starts = str.startswith("hi")  # checks if string starts with a specific substring
print("string not starts with hi",not_starts)   

#replace
replaced = str.replace("world","universe")  # replaces a substring with another substring
print("replaced string",replaced)

# find
found = str.find("welcome")  # finds the index of a substring
print("index of welcome",found) 

# count
counted = str.count("o")  # counts occurrences of a substring
print("count of o",counted) 

# length
length = len(str)  # gets the length of the string
print("length of the string",length)    

count= str.count("a")
print("count of a",count)

# index
index = str.index("python")  # finds the index of a substring (raises error if not found)
print("index of python",index)  

# split
split = str.split(",")  # splits the string into a list based on a delimiter
print("split string",split) 

# strip
str_with_spaces = "   hello world   "   # string with leading and trailing spaces
stripped = str_with_spaces.strip()  # removes leading and trailing whitespace
print("stripped string",stripped)           

# join
words = ["hello", "world"]  # list of words to join
joined = " ".join(words)  # joins the list into a single string with spaces
print("joined string",joined)

# isalpha
is_alpha = str.isalpha()  # checks if all characters are alphabetic 
print("is alpha",is_alpha)          

# isdigit
is_digit = str.isdigit()  # checks if all characters are digits             

print("is digit",is_digit)      

# isspace
space_str = "   "  # string with only spaces            

is_space = space_str.isspace()  # checks if all characters are whitespace
print("is space",is_space)
# title
title = str.title()  # converts to title case
print("title case",title)   
