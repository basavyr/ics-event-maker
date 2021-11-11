#!/usr/bin/env python

from icalendar import Calendar, Event
import pytz
from datetime import datetime
import os
from pathlib import Path

import icalendar as ical


print(ical.__version__)
print(Calendar.__name__)


cal = Calendar()
