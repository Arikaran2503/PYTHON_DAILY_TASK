student = {
    "name": "Arikaran",
    "age": 20
}

# Add an item
student["mark"] = 85
print("After adding:", student)

# Update an item
student["age"] = 21
print("After updating:", student)

# Check whether a key exists
print("name" in student)
print("course" in student)

# Delete an item
del student["mark"]
print("After deleting:", student)

# Find dictionary length
print("Total items:", len(student))
