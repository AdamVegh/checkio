__author__ = 'Vegh Adam'

from datetime import datetime


def days_diff(date1, date2):
    return abs(datetime(*date2) - datetime(*date1)).total_seconds() / (60*60*24)
