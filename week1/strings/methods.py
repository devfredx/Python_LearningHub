message = "python progrAMming LANguage"

# makes the first letter of the sentence capitalized
x = message.capitalize()
print(x)

# makes all letters of the string lowercase
x = message.casefold()
print(x)

# returns the number of times the corresponding word appears in the String
x = message.count("programming")
print(x)

# checks if the corresponding character is in the string
x = message.endswith(".")
print(x)

# shows the index where the character starts in the string
x = message.find("python")
print(x)

x = message.index("python")
print(x)

# checks the alphanumericity of all characters in the text
x = message.isalnum()
print(x)

# checks if all characters in the text are letters
txt = "fred"
x = txt.isalpha()
print(x)

# checks if all characters in the text are ascii characters
x = txt.isascii()
print(x)

# checks if all characters in a string are decimal numbers
a = "123436767"
x = a.isdecimal()
print(x)

# checks if all characters in the text are digits
x = a.isdigit()
print(x)

# checks whether all characters in the text are lowercase
x = txt.islower()
print(x)

# checks if all characters in the text are capitalized
x = txt.isupper()
print(x)

# checks if all characters in the text are numeric
x = txt.isnumeric()
print(x)

# checks if all characters in the text are printable
x = message.isprintable()
print(x)

# checks whether each word starts with a capital letter
x = message.istitle()
print(x)

# check if the string starts with the corresponding character
x = message.startswith("python")
print(x)

# makes lowercase letters uppercase and uppercase letters lowercase
x = message.swapcase()
print(x)

# makes the first letter of each word capitalized
x = message.title()
print(x)