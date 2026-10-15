# Tip calculator

Solution for the exercise in session 1 of **Introduction to Python** at HDBW.

Ask for the bill amount, the tip percentage and the number of people, then print the total and the amount per person, rounded to 2 decimals.

```
Bill: 84
Tip %: 10
People: 3
Total: 92.40 EUR, each pays 30.80 EUR
```

## Files

| File | What it does |
|---|---|
| `tip_calculator.py` | The main solution |
| `extensions/level1_show_tip.py` | Level 1: also prints the tip amount |
| `extensions/level2_percent_sign.py` | Level 2: accepts input like `15%` |
| `extensions/level3_round_up.py` | Level 3: each person pays a whole euro amount, rounded up |
| `tests/test_tip_calculator.py` | Automatic checks for all four programs |

## Run it

```
python3 tip_calculator.py
```

Or paste the code into a cell in [Google Colab](https://colab.research.google.com) and press Shift + Enter.

## Run the tests

```
pip install pytest
python3 -m pytest
```

## What breaks it?

Try typing `abc` as the bill or `0` people. The program crashes with a `ValueError` or a `ZeroDivisionError`. Later in the course we handle these cases with `if` and `try / except`.
