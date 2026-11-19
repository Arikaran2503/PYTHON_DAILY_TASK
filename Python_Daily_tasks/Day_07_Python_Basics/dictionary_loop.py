student = {
    "name": "Arikaran",
    "age": 20,
    "course": "Python Full Stack"
}

# Loop through keys
print("Student Details:")

for key in student:
    print(key, ":", student[key])

# Loop through key-value pairs
print("\nUsing items():")

for key, value in student.items():
    print(key, "=", value)
