# Try it: seconds converter
# Turn a number of seconds into hours, minutes and seconds.

seconds = int(input("Seconds: "))

hours = seconds // 3600
minutes = seconds % 3600 // 60
rest = seconds % 60

print(f"{hours}h {minutes}min {rest}s")
