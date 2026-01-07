v = ["fred", "python"]
x = 2
y = 5
z = x

# Exponentiation
print(x ** y)

# Returns True if both statements are true
print(x > 3 and x < 10)

# Returns True if one of the statements is true
print(x > 3 or x < 4)

# Reverse the result, returns False if the result is true
print(not(x > 3 and x < 10))

# Returns True if both variables are the same object
print(x is z)
print(x is y)
print(x == y)

# Returns True if both variables are not the same object
print(x is not z)
print(x is not y)
print(x != y)

# Returns True if a sequence with the specified value is present in the object
print("python" in v)

# Returns True if a sequence with the specified value is not present in the object
print("java" not in v)