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


# cal = Calendar()
# Set ourselves as the calendar's owner, required by most servers
# cal.add('attendee', 'MAILTO:robert.poenaru@icloud.com')

# event = Event()
# event.add('summary', 'Test Event')
# event.add('dtstart', datetime(2019, 1, 1, 10, 0, 0, tzinfo=pytz.UTC))
# event.add('dtend', datetime(2019, 1, 1, 11, 0, 0, tzinfo=pytz.UTC))
# event.add('dtstamp', datetime(2019, 1, 1, 10, 0, 0, tzinfo=pytz.UTC))
# event.add('description', 'This is a test event')


# # add event to calendar
# cal.add_component(event)

# print(cal)

# print(os.getcwd())

# with open('test.ics', 'wb') as f:
#     f.write(cal.to_ical())


def Create_iCal_Event(start, end, stamp, summary, description):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start)
    event.add('dtend', end)
    event.add('dtstamp', stamp)
    event.add('description', description)
    cal.add_component(event)
    return cal


def CreateDateTime(year, month, day, hour, minute, second):
    return datetime(year, month, day, hour, minute, second, tzinfo=pytz.UTC)


print(CreateDateTime(2019, 1, 1, 10, 0, 0))
