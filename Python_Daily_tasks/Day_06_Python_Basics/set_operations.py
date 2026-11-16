set1 = {10, 20, 30, 40}
set2 = {30, 40, 50, 60}

# Union
print("Union:", set1.union(set2))

# Intersection
print("Intersection:", set1.intersection(set2))

# Difference
print("Difference:", set1.difference(set2))

# Symmetric Difference
print("Symmetric Difference:", set1.symmetric_difference(set2))

# Subset
print("Is Subset:", {10, 20}.issubset(set1))

# Superset
print("Is Superset:", set1.issuperset({10, 20}))