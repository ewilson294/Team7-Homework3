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

# store days of each month in a standard 365 day year
calendar_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Print Header
table_header = 'Month Average  Minimum Maximum'
print(table_header)
print('=' * len(table_header))

# Gather Statistics for steps by month
month_code = 0 # separate index for month of the year
for month in calendar_days:
    month_code += 1 # increase by 1 for each month
    daily_steps = 0 # Initial condition for the amount of steps in the month
    minimum = None # Initial condition for the minimum
    maximum = None # Initial condition for the maximum
    for day in range(month):
        ds = steps.readline() # Hold the line as a string before converting
        ds = float(ds) # Convert the string into a float
        if maximum == None or maximum < ds:
            maximum = ds # keep the maximum amount of steps for the month
        if minimum == None or minimum > ds:
            minimum = ds # keep the minimum amount of steps for the month
        daily_steps += ds # keep a running total for the amount of steps in the month
    average = daily_steps/month # Calculate average amount of steps in a month
    # print a row of the table of summary statistics for every month
    print(format(month_code, '2d'), ' '*4, format(average, '7.2f'), ' '*5, format(minimum, '4.0f'), ' '*3, format(maximum, '5.0f'), sep='')
    
# Close steps.txt
steps.close()
