# Test cases for is_balanced
from brackets import is_balanced

assert is_balanced("print(len([1, 2]))")
assert is_balanced("{a: [1, (2)]}")
assert is_balanced("(a[b]{c})")
assert is_balanced("")
assert not is_balanced("(]")
assert not is_balanced("([)]")
assert not is_balanced("((")
assert not is_balanced(")(")
print("Alle Tests bestanden")
