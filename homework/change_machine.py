# Homework (challenge): change machine
# // tells how many coins fit, % tells what is left over.

cents = int(input("Amount in cents: "))

c200 = cents // 200
cents = cents % 200
c100 = cents // 100
cents = cents % 100
c50 = cents // 50
cents = cents % 50
c20 = cents // 20
cents = cents % 20
c10 = cents // 10
cents = cents % 10
c5 = cents // 5
cents = cents % 5
c2 = cents // 2
cents = cents % 2
c1 = cents

print(f"2 EUR: {c200}, 1 EUR: {c100}, 50 c: {c50}, 20 c: {c20}")
print(f"10 c: {c10}, 5 c: {c5}, 2 c: {c2}, 1 c: {c1}")
