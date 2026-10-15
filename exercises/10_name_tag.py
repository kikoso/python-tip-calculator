# Mini exercise 4: name tag
# Print a name in capital letters inside a frame of stars.

name = input("Name: ")

tag = name.upper()
border = "*" * (len(tag) + 4)

print(border)
print("* " + tag + " *")
print(border)
