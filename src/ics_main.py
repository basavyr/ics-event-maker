#!/usr/bin/env python

# local imports
import day_generator as day_gen
import cal_event_maker as event_maker
import package_tester

nov_first_work_day = 15
nov_day_id = 1
dec_first_work_day = 1
dec_day_id = 3
nov_last_day = 30
dec_last_day = 31

nov_month = [x for x in range(1, nov_last_day + 1)]
dec_month = [x for x in range(1, dec_last_day + 1)]

# generate the days for RT sessions for the month of November
nov_work_days = day_gen.generate_month_work_days(
    nov_first_work_day, nov_month, nov_day_id)
# generate the days for RT sessions for the month of December
dec_work_days = day_gen.generate_month_work_days(
    dec_first_work_day, dec_month, dec_day_id)


# Define calendar parameters
EMAIL = 'robert.poenaru@icloud.com'

# Generate a set of dates for the calendar
DESCRIPTION = "Radiotherapy sessions | B3"
SUMMARY = lambda id, month: f'☢️ RT Session-{id}-{month}'
YEAR = 2021
M_NOV = 11
M_DEC = 12

# define the RT start time and end time
START_SESSION = [11, 36, 0]
END_SESSION = [12, 30, 0]
STAMP = event_maker.datetime.utcnow()

LOCATION = 'Amethyst Radiotherapy Calea Odăii, 44, Otopeni, 030171, Romania'

# create datetime with the values given by the configured session constants
dt_start = lambda day, month: event_maker.CreateDateTime(
    YEAR, month, day, START_SESSION[0], START_SESSION[1], START_SESSION[2])

dt_end = lambda day, month: event_maker.CreateDateTime(
    YEAR, month, day, END_SESSION[0], END_SESSION[1], END_SESSION[2])

nov_start_datetimes = [dt_start(x, M_NOV) for x in nov_work_days]
dec_start_datetimes = [dt_start(x, M_DEC) for x in dec_work_days]

nov_end_datetimes = [dt_end(x, M_NOV) for x in nov_work_days]
dec_end_datetimes = [dt_end(x, M_DEC) for x in dec_work_days]


cal = package_tester.Calendar()
# Set ourselves as the calendar's owner, required by most servers
cal.add('attendee', f'MAILTO:{EMAIL}')

event = lambda start, end, id, month: event_maker.Create_iCal_Event(
    start, end, STAMP, SUMMARY(id, month), DESCRIPTION, LOCATION)

# create the list of sessions for November
nov_sessions = [event(nov_start_datetimes[id], nov_end_datetimes[id], id + 1, M_NOV)
                for id in range(len(nov_start_datetimes))]

dec_sessions = [event(dec_start_datetimes[id], dec_end_datetimes[id], id + 1, M_DEC)
                for id in range(len(dec_start_datetimes))]


# add the November sessions to the calendar
for session in nov_sessions:
    cal.add_component(session)

# add the December sessions to the calendar
for session in dec_sessions:
    cal.add_component(session)

with open('RT_Sessions.ics', 'wb') as f:
    f.write(cal.to_ical())
