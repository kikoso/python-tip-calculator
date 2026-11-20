# The array module: typed values stored directly in memory
from array import array

a = array("i", [1, 2, 3])
a.append(4)
print(a, a[0])

try:
    a.append("Hallo")
except TypeError as e:
    print("TypeError:", e)
