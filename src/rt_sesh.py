# import numpy as np
# import matplotlib.pyplot as plt

class Sessions():
    """For each session type, request the initial date and the number of sessions that are available as input"""

    @staticmethod
    def DateFormat(date):
        return f'{date}.12.2021'


    # generate the rt sessions
    @staticmethod
    def RT_Sessions(start_date,n_sesh):
        sessions=[]
        current_date=start_date
        for id in range(n_sesh):
            sessions.append(Sessions.DateFormat(current_date))
            current_date=current_date+7
        return sessions
    
    # generate the nutritional sessions
    @staticmethod
    def Nutrition_Session(start_date, n_sesh):
        return 1,1

    # generate the toxicology sessions
    @staticmethod
    def Toxicology_Session(start_date,n_sesh):
        return 1,1



print(Sessions.RT_Sessions(1,4))


