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

## In-class exercises (session 1)

| File | Exercise |
|---|---|
| `exercises/01_first_program.py` | Your first program: three lines about yourself |
| `exercises/02a_age_in_2030.py` | Variables, task A: how old will you be in 2030? |
| `exercises/02b_swap.py` | Variables, task B: swap two values |
| `exercises/03_what_type.py` | Quick check: what type is it? |
| `exercises/04_km_to_miles.py` | Input, process, output: kilometres to miles |
| `exercises/05_seconds_converter.py` | Seconds to hours, minutes and seconds |
| `exercises/06_predict_output.py` | Quick check: predict the output |
| `exercises/07_age_in_days.py` | Mini exercise 1: age in days |
| `exercises/08_pizza.py` | Mini exercise 2: sharing pizza with // and % |
| `exercises/09_currency.py` | Mini exercise 3: euros to dollars |
| `exercises/10_name_tag.py` | Mini exercise 4: name tag with .upper() and len() |
| `exercises/11_grade_average.py` | Mini exercise 5: average of three grades |
| `exercises/12_travel_time.py` | Mini exercise 6: travel time in hours and minutes |

## Homework (session 1)

| File | Task |
|---|---|
| `homework/temperature.py` | Easy: Celsius to Fahrenheit |
| `homework/room_planner.py` | Medium: area, perimeter and flooring cost |
| `homework/change_machine.py` | Challenge: coins to give back |

## Run it

```
python3 tip_calculator.py
```

In PyCharm: open the file, right-click in the editor and choose **Run**. Type your input in the Run panel at the bottom.

## What breaks it?

Try typing `abc` as the bill or `0` people. The program crashes with a `ValueError` or a `ZeroDivisionError`. Later in the course we handle these cases with `if` and `try / except`.
