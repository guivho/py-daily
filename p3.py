# Time-stamp: <2025-08-08 08:49:06 p3.py Guivho>

"""

This module is called p3 in memory of my son Peter
It is collection of useful functions and subroutines

"""

import datetime
import os
import re
import time
import inspect

def dottify(number, width=0, align='>'):
    #TODO: check align is >, < or ^ and default to no <
    if width:
        n = f"{number:,}".replace(",", ".")
        return f"{n:{align}{width}}"
    else:
        return f"{number:,}".replace(",", ".")

def yso(date=''):
    if not isinstance(date, datetime.datetime):
        date = datetime.datetime.now()
    return f"{date.strftime('%Y-%m-%d')}"

def ymd(date=''):
    if not isinstance(date, datetime.datetime):
        date = datetime.datetime.now()
    return f"{date.strftime('%Y%m%d')}"

def hms(time=''):
    if not isinstance(time, datetime.datetime):
        time = datetime.datetime.now()
    return f"{time.strftime('%H:%M:%S')}"

class Log:

    logdir = r"c:\logs";

    def __init__(self, suffix):
        self.name = os.path.join(self.logdir, f"{ymd()}_{suffix}.log")

    def exists(self):
        return os.path.isfile(self.name)

    def touch(self):
        ts = datetime.datetime.now().timestamp()
        os.utime(self.name, (ts, ts))

    def log(self, tekst):
        with open(self.name, "a", encoding='utf-8') as handle:
            handle.write(f"{hms()} {tekst[:]}\n")


if __name__ == "__main__":
    print(ymd())
    print(yso())
    print(ymd(1234))
    print(hms())
    lg = Log("p3tst")
    lg.log("testje")
