#!/usr/bin/env python

# local imports
import day_generator as day_gen

nov_first_work_day = 15
dec_first_work_day = 1

nov_last_day = 30
dec_last_day = 31

nov_month = [x for x in range(1, nov_last_day + 1)]
dec_month = [x for x in range(1, dec_last_day + 1)]

# generate the days for RT sessions for the month of November
nov_work_days = day_gen.generate_month_work_days(
    nov_first_work_day, nov_month)
# generate the days for RT sessions for the month of December
dec_work_days = day_gen.generate_month_work_days(
    dec_first_work_day, dec_month)


# Define calendar parameters
EMAIL = 'robert.poenaru@icloud.com'

# Generate a set of dates for the calendar
DESCRIPTION = "Radiotherapy sessions | B3"
SUMMARY = lambda id: f'☢️ RT Session-{id}'
YEAR = 2021
M_NOV = 11
M_DEC = 12
D_NOV = [x for x in range(15, 31)]
D_DEC = [x for x in range(1, 32)]

# define the RT start time and end time
START_SESSION = [11, 36, 0]
END_SESSION = [12, 30, 0]