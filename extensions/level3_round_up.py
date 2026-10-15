# Level 3: each person pays a whole euro amount, rounded up
# Idea: work in cents, then use // to get whole euros

bill = float(input("Bill: "))
tip = int(input("Tip %: "))
people = int(input("People: "))

total = bill * (1 + tip / 100)
per_person = total / people

# 30.80 EUR -> 3080 cents (round() removes tiny float errors)
cents = round(per_person * 100)

# Adding 99 cents before // 100 rounds up: 3080 -> 31, 3000 -> 30
euros = (cents + 99) // 100

print(f"Total: {total:.2f} EUR, each pays {euros} EUR")
print(f"Collected: {euros * people} EUR, extra tip: {euros * people - total:.2f} EUR")
