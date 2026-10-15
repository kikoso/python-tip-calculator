# Level 3: each person pays a whole euro amount, rounded up
# Only // and %, no imports

bill = float(input("Bill: "))
tip = int(input("Tip %: "))
people = int(input("People: "))

total = bill * (1 + tip / 100)
per_person = total / people

# per_person // 1 gives the whole euros
# per_person % 1 > 0 is True (counts as 1) if there are any cents left over
euros = int(per_person // 1 + (per_person % 1 > 0))

print(f"Total: {total:.2f} EUR, each pays {euros} EUR")
print(f"Collected: {euros * people} EUR, extra tip: {euros * people - total:.2f} EUR")
