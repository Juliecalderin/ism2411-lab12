# Reflection
#
# Q1: How does a Python ETL pipeline compare to doing the same task in Excel?
# In Excel I would open the file, filter the rows, and copy the results into a
# new sheet by hand. In Python I write the steps once and the script repeats
# them exactly, so it handles huge files and new data without extra work.
# Excel is still easier for quick one-off looks, formatting, and charts.
#
# Q2: What business process would benefit from an append-mode log file?
# A store could log every sales report run, or every order that comes in,
# with a timestamp and the total. Append mode is the right tool because it adds
# a new line each time without erasing the old history, so you keep a full
# record you can check later.

import csv
from datetime import datetime

# Exercise 1: confirm the file opens
with open("data/sales.csv", newline="") as f:
    print("Exercise 1: sales.csv opened OK")

# Exercise 2: read and print raw rows (all values are strings)
print("\nExercise 2: raw rows")
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Exercise 3: skip the header with next()
print("\nExercise 3: skip header")
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print("Header:", header)
    for row in reader:
        print(row)

# Exercise 4: compute totals
print("\nExercise 4: totals")
total_revenue = 0
with open("data/sales.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        qty = int(row[2])
        total = price * qty
        total_revenue += total
        print(f"{product}: {qty} units × ${price:.2f} = ${total:.2f}")
print(f"Total revenue: ${total_revenue:.2f}")
