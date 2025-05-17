student = {
    "name": "Fury",
    "age": 20,
    "marks": [85, 90, 92]
}

# 2. Accessing values
print(student["name"])        
print(student.get("age"))     

# 3. Adding / Updating
student["city"] = "Karachi" 
student["age"] = 21           

# 4. Removing keys
student.pop("city")
del student["marks"]

# 5. Looping through dictionary
for key, value in student.items():
    print(key, ":", value)

# 6. Check if key exists
if "name" in student:
    print("Name exists")

# 7. Dictionary methods
keys = student.keys()
values = student.values()
items = student.items()

print("Keys:", keys)
print("Values:", values)
print("Items:", items)

# 8. Nested dictionary
students = {
    "101": {"name": "Ali", "age": 20},
    "102": {"name": "Sara", "age": 22}
}
print(students["102"]["name"])
