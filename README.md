# Python course solutions (HDBW)

Solutions for the exercises in **Softwareentwicklung und Programmieren 3** at HDBW. Session 1 is in the top-level folders, session 2 in `session2/`.

## Session 1: tip calculator

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

## Find the bug (session 1)

| File | Bug |
|---|---|
| `bugs/bug1_age_next_year.py` | input() returns a str |
| `bugs/bug2_greeting.py` | missing f before the string |
| `bugs/bug3_receipt.py` | Print with a capital P |
| `bugs/bug4_price.py` | joining a str and a float with + |
| `bugs/bug5_average.py` | missing brackets (precedence) |
| `bugs/bug6_hours_minutes.py` | / instead of // |

## Homework (session 1)

| File | Task |
|---|---|
| `homework/temperature.py` | Easy: Celsius to Fahrenheit |
| `homework/room_planner.py` | Medium: area, perimeter and flooring cost |
| `homework/change_machine.py` | Challenge: coins to give back |

## Session 2: functions, modules and exceptions

| File | Exercise |
|---|---|
| `session2/warmup/01_fizzbuzz.py` | FizzBuzz from 1 to 15 |
| `session2/warmup/02_list_statistics.py` | Sum, average and maximum with a loop |
| `session2/functions/01_temperature.py` | celsius_to_fahrenheit as a function |
| `session2/functions/02_leap_year.py` | is_leap_year with docstring and type hints |
| `session2/functions/03_grade.py` | grade(points) with early return |
| `session2/functions/04_sort_with_key.py` | sorted with key and a list comprehension |
| `session2/modules/text_tools.py`, `main.py` | Your own module and how to import it |
| `session2/exceptions/01_safe_divide.py` | try / except ZeroDivisionError |
| `session2/exceptions/02_read_int.py` | Ask until the input is valid |
| `session2/exceptions/03_account.py` | Account with its own exception |
| `session2/bugs/` | The six find-the-bug exercises, fixed |
| `session2/calculator/` | Robust calculator: `calculator.py` and `main.py` |
| `session2/calculator/level1_history/` | Level 1: history of all calculations |
| `session2/calculator/level2_operations/` | Level 2: ** and % with a dictionary of functions |
| `session2/calculator/level3_own_exception/` | Level 3: CalculatorError for all errors |
| `session2/mini/` | Four mini exercises: vowels, word lengths, safe average, discount |

The calculator and the module exercise each need both files in the same folder. Run `main.py` from that folder.

## Run it

```
python3 tip_calculator.py
```

In PyCharm: open the file, right-click in the editor and choose **Run**. Type your input in the Run panel at the bottom.

## What breaks it?

Try typing `abc` as the bill or `0` people. The program crashes with a `ValueError` or a `ZeroDivisionError`. Later in the course we handle these cases with `if` and `try / except`.
