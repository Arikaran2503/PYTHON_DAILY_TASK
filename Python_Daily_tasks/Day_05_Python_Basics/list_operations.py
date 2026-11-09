list1 = [10, 20, 30]
list2 = [40, 50, 60]

# Concatenation
result = list1 + list2
print("Concatenation:", result)

# Repetition
print("Repetition:", list1 * 2)

# Membership
print("20 in list1:", 20 in list1)
print("100 not in list1:", 100 not in list1)

# Updating Elements
list1[0] = 100
print("Updated List:", list1)

# Adding Elements
list1.append(40)
print("Added Element:", list1)

# Deleting Elements
del list1[1]
print("Deleted Element:", list1)