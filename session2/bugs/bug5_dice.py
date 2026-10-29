# Find the bug 5: a file called random.py imports itself instead of the
# standard library module. Fix: rename the file, e.g. to dice.py.

import random

print(random.randint(1, 6))
