# Warm-up: sum, average and maximum of a list with a loop
# (with built-ins it would be sum(numbers) and max(numbers))

numbers = [4, 8, 15, 16, 23, 42]

total = 0
largest = numbers[0]
for n in numbers:
    total += n
    if n > largest:
        largest = n

print(f"Summe: {total}")
print(f"Schnitt: {total / len(numbers)}")
print(f"Maximum: {largest}")
