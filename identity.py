# When to use
# To check if two variables point to the same object in memory.

# "is", returns True if both refer to the same object!
a = ["pencil" , "eraser"]
b = ["pencil" , "eraser"]
c = a

print(a is c)
print(a is b) #though they both have same content but they are not same!
print(a == b)

# "is not", returns True if they refer to different objects

a = ["pencil" , "eraser"]
b = ["pencil" , "eraser"]
c = a
print(a is not c)
print(a is not b)
print(a != b)
