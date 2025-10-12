student = {"name": "John", "marks": {"math": 80, "science": 75}}

new_marks = student.update({"marks": {"math": 90, "science": 80}})
print(student)
print(student["marks"]["math"])
student["marks"]["math"] = 95
print(student)