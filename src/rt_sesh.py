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
for day in range(RT_START_DATE, 31, 7):
    rt_day = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                        RT_START_HOUR[0], RT_START_HOUR[1], RT_START_HOUR[2])
    print(rt_day)

# show the dates for nutrition
for day in range(NUTRITION_START_DATE, 31, 7):
    nutrition_day = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                               NUTRITION_START_HOUR[0], NUTRITION_START_HOUR[1], NUTRITION_START_HOUR[2])
    print(nutrition_day)

# show the dates for toxicology
for day in range(NUTRITION_START_DATE, 31, 7):
    toxicology_day = event_maker.CreateDateTime(YEAR, M_DEC, day,
                                                TOXIC_START_HOUR[0], TOXIC_START_HOUR[1], TOXIC_START_HOUR[2])
    print(toxicology_day)
