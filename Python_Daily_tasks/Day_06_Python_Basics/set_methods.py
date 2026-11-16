fruits = {"Apple", "Banana", "Mango"}

# Add
fruits.add("Orange")
print("Add:", fruits)

# Update
fruits.update(["Grapes", "Pineapple"])
print("Update:", fruits)

# Remove
fruits.remove("Banana")
print("Remove:", fruits)

# Discard
fruits.discard("Apple")
print("Discard:", fruits)

# Pop
fruits.pop()
print("Pop:", fruits)

# Copy
new_fruits = fruits.copy()
print("Copy:", new_fruits)

# Clear
fruits.clear()
print("Clear:", fruits)