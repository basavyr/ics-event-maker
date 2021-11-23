# import numpy as np
# import matplotlib.pyplot as plt

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


RT_START_DATE = 30
RT_START_HOUR = [12, 10, 00]
RT_DESCRIPTION = ''
TOXIC_START_DATE = 26
TOXIC_START_HOUR = [12, 00, 00]
TOXIC_DESCRIPTION = ''
NUTRITION_START_DATE = 29
NUTRITION_START_HOUR = [12, 10, 00]
NUTRITION_DESCRIPTION = ''
