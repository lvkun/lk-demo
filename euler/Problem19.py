#-------------------------------------------------------------------------------
# Name:     Problem 19
# Purpose:
#           You are given the following information, 
#           but you may prefer to do some research for yourself.
#
#           1 Jan 1900 was a Monday.
#           Thirty days has September, April, June and November.
#           All the rest have thirty-one,
#           Saving February alone,
#           Which has twenty-eight, rain or shine.
#           And on leap years, twenty-nine.
#           A leap year occurs on any year evenly divisible by 4, 
#           but not on a century unless it is divisible by 400.
#           
#           How many Sundays fell on the first of the month during 
#           the twentieth century (1 Jan 1901 to 31 Dec 2000)?
# Link:     http://projecteuler.net/index.php?section=problems&id=5
# Author:   brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

month_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    if (year % 400 == 0):
        return True
    elif (year % 4 == 0 and year % 100 != 0):
        return True

    return False

def main():

    first_day = 1 # 1901-1-1 Tuesday
    sum_sundays = 0
    
    for year in xrange(1901,2001):

        for month in xrange(1, 13):

            if first_day == 6:
                sum_sundays += 1
            
            days = month_day[month-1]

            if month == 2 and is_leap_year(year):
                days = 29

            first_day = (first_day + days) % 7

    print sum_sundays


if __name__ == '__main__':
    main()
