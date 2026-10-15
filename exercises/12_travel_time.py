# Mini exercise 6: travel time
# Distance in km and speed in km/h. Show the travel time in hours and minutes.

distance = float(input("Distance: "))
speed = float(input("Speed: "))

minutes = round(distance / speed * 60)
hours = minutes // 60
rest = minutes % 60

print(f"{hours}h {rest}min")
