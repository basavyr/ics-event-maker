#!/usr/bin/env python

# uses the icalendar module to generate an iCalendar file
from icalendar import Calendar, Event
import pytz
from datetime import datetime
import os
from pathlib import Path

import icalendar as ical

if __name__ == "__main__":
    # check if the imported modules are working
    print(ical.__version__)
    print(Calendar.__name__)
