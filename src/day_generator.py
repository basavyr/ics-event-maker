#!/usr/bin/env python

def generate_month_work_days(month_first_work_day, month_days):
    """
    generate the list of working days based on the first day configured by the user
    """
    work_days = []
    id = 1
    for count in range(month_first_work_day - 1, len(month_days)):
        if(id <= 5):
            work_days.append(month_days[count])
            id += 1
        elif(id == 6):
            # skip a free day
            id += 1
        elif(id == 7):
            # skip a free day
            # reset the index
            id = 1

    return work_days
