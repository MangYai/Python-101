# Example of the identity operator

# Two variables pointing to the same list object
a =[1, 2, 3]
b = a

# Two variables pointing to different list objects with the same content
c = [1, 2, 3]
d = [1, 2, 3]

# Using the identity operator
print(a is b)  # True
print(a is c)  # False
print(c is d)  # False

# Using the equality operator for comparison
print(a == c) # True
print(c == d) # True
