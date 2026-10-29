# Find the bug 1: without return the function gives None


def gross(net):
    result = net * 1.19
    return result


price = gross(100)
print(f"{price:.2f} EUR")
