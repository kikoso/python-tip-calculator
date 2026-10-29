# Find the bug 2: a list as default value is created only once
# Fix: None as placeholder, then a new list on every call


def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items


print(add_item("Milch"))
print(add_item("Brot"))
