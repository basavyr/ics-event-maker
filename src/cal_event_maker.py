#!/usr/bin/env python

# uses the icalendar module to generate an iCalendar file
from icalendar import Calendar, Event
import pytz
from pytz import timezone
from datetime import datetime
import os
from pathlib import Path


def CreateDateTime(year, month, day, hour, minute, second):
    """generate a proper datetime that will ve used in the icalendar file"""
    return datetime(year, month, day, hour, minute, second, tzinfo=timezone('Europe/Bucharest'))


def Create_iCal_Event(start, end, stamp, summary, description):
    event = Event()
    event.add('summary', summary)
    event.add('dtstart', start)
    event.add('dtend', end)
    event.add('dtstamp', stamp)
    event.add('description', description)
    return event
