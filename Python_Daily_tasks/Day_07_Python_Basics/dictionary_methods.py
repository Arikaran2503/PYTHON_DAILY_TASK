student = {
    "name": "Arikaran",
    "age": 20,
    "course": "Python"
}

# Adding a new item
student["city"] = "Tiruchendur"
print("After adding:", student)

# Updating a value
student.update({"age": 21})
print("After updating:", student)

# Removing an item
student.pop("course")
print("After removing:", student)

# Display dictionary items
print("Items:", student.items())
