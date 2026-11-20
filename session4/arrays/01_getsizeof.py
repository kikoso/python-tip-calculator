# The list grows in jumps: reserve slots are filled by append without moving
import sys

lst = []
for i in range(17):
    lst.append(i)
    print(len(lst), sys.getsizeof(lst))
