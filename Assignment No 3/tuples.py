# Create Tuples
t1 = (1,2,3,4,5,6,7,8,9, 10.23)
t2= ("apple", "banana", "orange", "kiwi")

print(t1[0])    
print(t2[-1])      

# 3. Slicing
print(t1[1:])   

# 4. Nested tuples
nested = (1, (2, 3), (4, 5))
print(nested[1][0])  # 2

# 6. Looping
for item in t2:
    print(item)

# 7. Immutability (tuples can't be changed)
# t1[0] = 99  

# 8. Tuple methods
print(t1.count(2))   
print(t1.index(3))   