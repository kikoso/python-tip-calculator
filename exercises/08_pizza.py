# Mini exercise 2: sharing pizza
# Every pizza has 8 slices. How many slices does each person get,
# and how many are left over?

pizzas = int(input("Pizzas: "))
people = int(input("People: "))

slices = pizzas * 8

print(f"Each person: {slices // people} slices")
print(f"Left over: {slices % people} slices")
