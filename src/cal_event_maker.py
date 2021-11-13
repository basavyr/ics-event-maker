#!/usr/bin/env python

# uses the icalendar module to generate an iCalendar file
from icalendar import Calendar, Event
import pytz
from datetime import datetime
import os
from pathlib import Path

nov_first_work_day = 15
dec_first_work_day = 1
nov_end_day = 30
dec_end_day = 31

nov_month_days = [x for x in range(1, nov_end_day + 1)]
dec_month_days = [x for x in range(1, dec_end_day + 1)]

