# Standard Library
from calendar import HTMLCalendar
from datetime import datetime, timedelta

# Third Party
from games.models import Game


class Calendar(HTMLCalendar):
    cssclasses_weekday_head = [
        style + " text-bold" for style in HTMLCalendar.cssclasses
    ]
    cssclass_month_head = "display-6 text-bold"

    def __init__(self, year=None, month=None):
        self.year = year
        self.month = month
        super(Calendar, self).__init__()

    # formats a day as a td
    # filter events by day
    def formatday(self, day, events):
        events_per_day = events.filter(start_time__day=day)
        d = ""
        for event in events_per_day:
            d += f"<li>{event.game_day}. Spieltag {event.team.name} </li>"

        if day != 0:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
        return "<td></td>"

    # formats a week as a tr
    def formatweek(self, theweek, events):
        week = ""
        for d, weekday in theweek:
            week += self.formatday(d, events)
        return f"<tr> {week} </tr>"

    # formats a month as a table
    # filter events by year and month
    def formatmonth(self, withyear=True):
        events = Game.objects.filter(
            start_time__year=self.year, start_time__month=self.month
        )

        cal = f'<div class="table-responsive-lg"><table border="0" cellpadding="0" cellspacing="0" class="table calendar">\n'
        cal += f"{self.formatmonthname(self.year, self.month, withyear=withyear)}\n"
        cal += f"{self.formatweekheader()}\n"
        for week in self.monthdays2calendar(self.year, self.month):
            cal += f"{self.formatweek(week, events)}\n"
        return cal
