results = {
     "name": "John",
     "age": 19,
     "subjects": {
            "maths": 84,
            "science": 78,
            "history": 90
     }
}   

results["subjects"]["maths"] = 95
print(results)

print(type(results))
# nested dictionary
print(results["subjects"]["maths"])
