# Lists
numbers = [1,2,3,4,5]
letters = ["a", "b", "d", "e", "f"]

# Accessing Elements
print(numbers[0])
print(letters[4])

# slicing
print(numbers[2:])

# ADD ITEMS
numbers.append(6)
numbers.insert(2,85)
print(numbers)

# Remove items
letters.remove("a")
letters.pop() #removes the last element if not value asigned
print(letters)

# Loops
for numeric in numbers:
    print(numeric)

# check membership 
print("e" in letters)

# Copy list safely
copy = numbers[:]
numbers.append(100)
print("Copy:", copy)