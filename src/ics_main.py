#!/usr/bin/env python

# local imports
import day_generator as day_gen


nov_first_work_day = 15
dec_first_work_day = 1

nov_last_day = 30
dec_last_day = 31

nov_month = [x for x in range(1, nov_last_day + 1)]
dec_month = [x for x in range(1, dec_last_day + 1)]

nov_work_days = day_gen.generate_month_work_days(
    nov_first_work_day, nov_month)
dec_work_days = day_gen.generate_month_work_days(
    dec_first_work_day, dec_month)
print(nov_work_days)
print(dec_work_days)
