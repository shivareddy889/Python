# methods of dictionary
dict1 = {
    "name" : "shiva",   
    "age" : 20,
    "city" : "hyd",
    "subjects" : {
        "maths" : 90,
        "science" : 85,     
        "history" : 88

    }

}
print(dict1)
print(type(dict1))
# get method
print(dict1.get("name"))
print(dict1.get("subjects").get("maths"))

# keys method
print(dict1.keys())
print(dict1.get("subjects").keys())

# values method
print(dict1.values())
print(dict1.get("subjects").values())

# items method
print(dict1.items())
print(dict1.get("subjects").items())

# clear method
dict1.clear()
print(dict1)

# copy method
dict2 = {
    "name" : "ram",   
    "age" : 22,
    "city" : "delhi"
}
dict3 = dict2.copy()
print(dict3)
print(type(dict3))

# update method
dict3.update({"age":23})
print(dict3)
dict3.update({"country":"India"})
print(dict3)    

print(dict1.get("laptop", "no value"))  # will return None since dict1 is cleared

# setdefault method
dict3.setdefault("age", 24)  # will not change since age key already exists

print(dict3)
dict3.setdefault("phone", "1234567890")  # will add since phone key
print(dict3)
