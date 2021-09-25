""" 
Homework 3
Problem 2
Team#: 7
Team Member-1: Eric Wilson - Member’s Contribution 33%
Team Member-2: Ha Tran - Member’s Contribution 33%
Team Member-3: Quynh Tran - Member’s Contribution 33%
"""

# open steps.txt 
steps = open('steps.txt')
# store days of each month in a standard 365 day year (VERIFY)
calendar_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
# Print Header
table_header = 'Month Average  Minimum Maximum'
print(table_header)
print('=' * len(table_header))
# Gather Statistics for steps by month
for month in calendar_days:
    daily_steps = 0
    minimum = None
    maximum = None
    for day in range(month):
        ds = steps.readline() # Hold the line as a string before converting
        ds = float(ds[:-1])
        if maximum == None or maximum < ds:
            maximum = ds
        if minimum == None or minimum > ds:
            minimum = ds
        daily_steps += ds
    average = daily_steps/month
    print(month, format(average, '4.2f'), format(minimum, '4.0f'), format(maximum, '5.0f'), sep=' ')
steps.close()