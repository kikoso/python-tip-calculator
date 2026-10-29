# Functions 3: grade for a number of points (early return)


def grade(points: int) -> str:
    """Return the grade for the given points."""
    if points >= 90:
        return "sehr gut"
    if points >= 80:
        return "gut"
    if points >= 65:
        return "befriedigend"
    if points >= 50:
        return "ausreichend"
    return "nicht bestanden"


for p in [95, 72, 40]:
    print(grade(p))
