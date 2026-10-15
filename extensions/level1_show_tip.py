# Level 1: show the tip amount on its own line, before the total

bill = float(input("Bill: "))
tip = int(input("Tip %: "))
people = int(input("People: "))

tip_amount = bill * tip / 100
total = bill + tip_amount
per_person = total / people

print(f"Tip: {tip_amount:.2f} EUR")
print(f"Total: {total:.2f} EUR, each pays {per_person:.2f} EUR")
