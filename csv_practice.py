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
