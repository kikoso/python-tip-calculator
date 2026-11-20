# Exercise: moving average over the last size values
from collections import deque


def moving_average(values, size):
    window = deque(maxlen=size)
    result = []
    for x in values:
        window.append(x)
        result.append(sum(window) / len(window))
    return result


print(moving_average([10, 20, 30, 40, 50], 3))
