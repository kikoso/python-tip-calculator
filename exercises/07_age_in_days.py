# Mini exercise 1: age in days
# Roughly how many days old are you? Every fourth year has one extra day.

years = int(input("Age: "))

days = years * 365 + years // 4

print(f"About {days} days")
