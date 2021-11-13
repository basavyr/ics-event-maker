#!/usr/bin/env python


nov_first_work_day = 15
dec_first_work_day = 1
nov_end_day = 30
dec_end_day = 31

nov_month_days = [x for x in range(1, nov_end_day + 1)]
dec_month_days = [x for x in range(1, dec_end_day + 1)]


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


if __name__ == "__main__":
    nov_work_days = generate_month_work_days(
        nov_first_work_day, nov_month_days)
    dec_work_days = generate_month_work_days(
        dec_first_work_day, dec_month_days)
    print(f'November: {nov_work_days}')
    print(f'December: {dec_work_days}')
