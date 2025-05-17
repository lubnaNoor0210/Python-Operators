# SET: IS unordered, unchangeable, unindexed, mutable!
# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.
# Curly braces or the set() function can be used to create sets.
#  Note: to create an empty set you have to use set(), not {}



# 1. Creating sets
s1 = {1, 2, 3, 4}
s2 = set([3, 4, 5, 6])

print("Set 1:", s1)
print("Set 2:", s2)

# 2. Set operations
print("Union:", s1 | s2)
print("Intersection:", s1 & s2)
print("Difference:", s1 - s2)
print("Symmetric Difference:", s1 ^ s2)

# 3. Modifying sets
s1.add(10)
s1.update([11, 12])
s1.remove(2)     # it will raise error if not found
s1.discard(99)  # safer way to avoid errors if the values are not found
print("Modified Set 1:", s1)

# 4. Looping through set
for item in s2:
    print("Item in Set 2:", item)

# 5. Set properties
print("Length:", len(s2))
print("Is 5 in set?", 5 in s2)

# 6. Frozen set (immutable)
fs = frozenset([1, 2, 3, 4])
print("Frozen set:", fs)

# fs.add(5)  
# fs.remove(2)  

# You can still use set operations
print("Frozen set union:", fs.union([5, 6]))
