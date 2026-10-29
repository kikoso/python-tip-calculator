# Functions 4: sorting with key and a list comprehension

products = [("Kaffee", 4.5), ("Tee", 2.0), ("Kakao", 3.2)]

by_price = sorted(products, key=lambda p: p[1])
print(by_price)

cheap = [name for name, price in products if price < 4]
print(cheap)
