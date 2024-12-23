"""Snippets for the datetime module.

# Links

- [Python's strftime directives](https://strftime.org)
- [datetime documentation](https://docs.python.org/3/library/datetime.html)
- [tz database](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)
- [guide](http://pytz.sourceforge.net/)  # for pytz only
- <https://blog.ganssle.io/articles/2019/11/utcnow.html>
"""

import zoneinfo
from datetime import datetime, timedelta, timezone
from zoneinfo import ZoneInfo

# show available timezones
zoneinfo.available_timezones()

# get current time in utc
date = datetime.now(timezone.utc)

# convert utctimestamp to aware datetime
datetime.fromtimestamp(0, tz=timezone.utc)

# get current time in Oslo, Norway
date = datetime.now(tz=ZoneInfo("Europe/Oslo"))

# create specific time in timezone
date = datetime(2020, 10, 5, 3, 9, tzinfo=ZoneInfo("America/Vancouver"))
# convert to a different timezone
date = date.astimezone(ZoneInfo("Europe/Oslo"))

datetime.fromisoformat(datetime.now(tz=timezone.utc).isoformat())


def absolute_add(date: datetime, delta: timedelta) -> datetime:
    """Add time to date using absolute time semantics."""
    date_utc = date.astimezone(timezone.utc)
    date_utc += delta
    return date_utc.astimezone(date.tzinfo)


def absolute_diff(date1: datetime, date2: datetime) -> timedelta:
    """Get difference between two dates using absolute time semantics."""
    return date1.astimezone(timezone.utc) - date2.astimezone(timezone.utc)
