#SOLVED
#How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
#Iterate through years, Iterate through months, starting param is the day of the week of the day before the 1st
#Monday = 1, if module 7 then it is a Sunday
months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthsLeap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 2
sundaySum = 0
for year in range(1901, 2001):
    for month in range(12):
        if(day % 7 ==0):
            sundaySum += 1
        if(year%4 ==0):
            day += monthsLeap[month]
        else:
            day += months[month]
print(sundaySum)