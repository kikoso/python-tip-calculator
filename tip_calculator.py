# Tip calculator
# Introduction to Python, session 1 (HDBW)
#
# Input -> Process -> Output

# 1. Input: input() always returns text, so convert it
bill = float(input("Bill: "))
tip = int(input("Tip %: "))
people = int(input("People: "))

# 2. Process
total = bill * (1 + tip / 100)
per_person = total / people

# 3. Output: :.2f shows 2 decimal places
print(f"Total: {total:.2f} EUR, each pays {per_person:.2f} EUR")
