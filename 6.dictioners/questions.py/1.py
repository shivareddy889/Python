
# Create a dictionary named profile with keys "name", "age", and "city".
profile = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",

}

print(profile)
print(type(profile))
print(profile["name"])
print(profile["age"])

# Add a new key "country" with the value "USA" to the profile dictionary.
update = profile.update({"country": "India"})

# Update the age to 31.
print(profile)
new_age = profile.update({"age": 31})
print(profile)

# remove the age key from the dictionary.
del profile["age"]
print(profile)

print(profile.get("name"))