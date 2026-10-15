# Level 2: accept the tip as "15" or "15%"

bill = float(input("Bill: "))
tip = int(input("Tip %: ").strip("%"))  # .strip("%") removes the % sign
people = int(input("People: "))

total = bill * (1 + tip / 100)
per_person = total / people

print(f"Total: {total:.2f} EUR, each pays {per_person:.2f} EUR")
