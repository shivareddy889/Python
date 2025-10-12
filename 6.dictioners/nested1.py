personal_info = {
     "name": input("Enter your name: "),
     "age": int(input("Enter your age: ")),
     "subjects": {
            "maths": int(input("Enter your maths score: ")),
            "science": int(input("Enter your science score: ")),
            "history": int(input("Enter your history score: "))
     },
     "teacher": ["sangeetha","Suresh","Ramesh"]

}
print(personal_info)
print(personal_info["subjects"]["maths"])
print(personal_info["teacher"][0])
