# Functions 2: leap year as a function, with docstring and type hints


def is_leap_year(year: int) -> bool:
    """Return True if year is a leap year."""
    div4 = year % 4 == 0
    div100 = year % 100 == 0
    div400 = year % 400 == 0
    return div4 and (not div100 or div400)


print(is_leap_year(2024))
print(is_leap_year(1900))
print(is_leap_year(2000))
