# Homework (medium): room planner

width = float(input("Width (m): "))
length = float(input("Length (m): "))
price = float(input("Flooring price per m²: "))

area = width * length
perimeter = 2 * (width + length)
cost = area * price

print(f"Area: {area:.2f} m²")
print(f"Perimeter: {perimeter:.2f} m")
print(f"Flooring cost: {cost:.2f} EUR")
