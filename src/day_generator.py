#!/usr/bin/env python

def generate_month_work_days(month_first_work_day, month_days, id_picker):
    """
    generate the list of working days based on the first day configured by the user
    the id_picker specifies which day of the week the month_first_work_day is, regarding the entire week
    """
    work_days = []
    id = id_picker
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
