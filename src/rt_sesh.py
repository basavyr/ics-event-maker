# import numpy as np
# import matplotlib.pyplot as plt


# local imports
import day_generator as day_gen
import cal_event_maker as event_maker
import package_tester


class Sessions():
    """For each session type, request the initial date and the number of sessions that are available as input"""

    @staticmethod
    def DateFormat(date):
        return f'{date}.12.2021'

    # generate the rt sessions

    @staticmethod
    def RT_Sessions(start_date, n_sesh):
        sessions = []
        current_date = start_date
        for id in range(n_sesh):
            sessions.append(Sessions.DateFormat(current_date))
            current_date = current_date + 7
        return sessions

    # generate the nutritional sessions
    @staticmethod
    def Nutrition_Session(start_date, n_sesh):
        return 1, 1

    # generate the toxicology sessions
    @staticmethod
    def Toxicology_Session(start_date, n_sesh):
        return 1, 1


# Define calendar parameters
EMAIL = 'robert.poenaru@icloud.com'

# set the default location for the calendar events
LOCATION = 'Amethyst Radiotherapy Calea Odăii, 44, Otopeni, 030171, Romania'
YEAR = 2021
M_NOV = 11
M_DEC = 12
STAMP = event_maker.datetime.utcnow()

# create datetime with the values given by the configured session constants
# dt_start = lambda day, month: event_maker.CreateDateTime(
#     YEAR, month, day, START_SESSION[0], START_SESSION[1], START_SESSION[2])

# dt_end = lambda day, month: event_maker.CreateDateTime(
# YEAR, month, day, END_SESSION[0], END_SESSION[1], END_SESSION[2])

RT_START_DATE = 7
RT_START_HOUR = [12, 10, 00]
RT_DESCRIPTION = '🩺 Radiology Consultation | Dr. Zarma'
TOXIC_START_DATE = 10
TOXIC_START_HOUR = [12, 00, 00]
TOXIC_DESCRIPTION = '☣️ Toxicity Consultation'
NUTRITION_START_DATE = 6
NUTRITION_START_HOUR = [12, 10, 00]
NUTRITION_DESCRIPTION = '🥗 Nutrition Consultation'

# show the dates for RT
RT_DAYS_START = []
RT_DAYS_END = []
for day in range(RT_START_DATE, 31, 7):
    rt_day_0 = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                          RT_START_HOUR[0], RT_START_HOUR[1], RT_START_HOUR[2])
    rt_day_1 = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                          RT_START_HOUR[0] + 1, RT_START_HOUR[1], RT_START_HOUR[2])
    RT_DAYS_START.append(rt_day_0)
    RT_DAYS_END.append(rt_day_1)


NUTRITION_DAYS_START = []
NUTRITION_DAYS_END = []
# show the dates for nutrition
for day in range(NUTRITION_START_DATE, 31, 7):
    nutrition_day_0 = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                                 NUTRITION_START_HOUR[0], NUTRITION_START_HOUR[1], NUTRITION_START_HOUR[2])
    nutrition_day_1 = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                                 NUTRITION_START_HOUR[0] + 1, NUTRITION_START_HOUR[1], NUTRITION_START_HOUR[2])
    NUTRITION_DAYS_START.append(nutrition_day_0)
    NUTRITION_DAYS_END.append(nutrition_day_1)


TOXIC_DAYS_START = []
TOXIC_DAYS_END = []
# show the dates for toxicology
for day in range(TOXIC_START_DATE, 31, 7):
    toxicology_day_0 = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                                  TOXIC_START_HOUR[0], TOXIC_START_HOUR[1], TOXIC_START_HOUR[2])
    toxicology_day_1 = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                                  TOXIC_START_HOUR[0] + 1, TOXIC_START_HOUR[1], TOXIC_START_HOUR[2])
    TOXIC_DAYS_START.append(toxicology_day_0)
    TOXIC_DAYS_END.append(toxicology_day_1)


cal = package_tester.Calendar()
# Set ourselves as the calendar's owner, required by most servers
cal.add('attendee', f'MAILTO:{EMAIL}')

# for id in range(len(RT_DAYS_START)):
#     cal.add_component(event_maker.Create_iCal_Event(
#         RT_DAYS_START[id], RT_DAYS_END[id], STAMP, RT_DESCRIPTION, RT_DESCRIPTION, LOCATION))

# with open('RT_Visits.ics', 'wb') as f:
#     f.write(cal.to_ical())

for id in range(len(NUTRITION_DAYS_START)):
    cal.add_component(event_maker.Create_iCal_Event(
        NUTRITION_DAYS_START[id], NUTRITION_DAYS_END[id], STAMP, NUTRITION_DESCRIPTION, NUTRITION_DESCRIPTION, LOCATION))

with open('NUTRITION_Visits.ics', 'wb') as f:
    f.write(cal.to_ical())
