# Mini exercise 3: currency converter
# Convert euros to dollars and show both with two decimals.
# Note: type 1.08, not 1,08.

euros = float(input("Euros: "))
rate = float(input("Rate: "))

dollars = euros * rate

print(f"{euros:.2f} EUR = {dollars:.2f} USD")
