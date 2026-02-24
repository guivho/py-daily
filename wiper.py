# Time-stamp: <2026-02-24 13:43:09 wiper.py Guivho>

import datetime
import os
import re
import time
import p3

class Counts:
    def __init__(self):
        self.nrsubdirs = 0
        self.nrsubwipd = 0
        self.nroffiles = 0
        self.nrfilwipd = 0
        self.nrofbytes = 0
        self.filwipers = 0
        self.dirwipers = 0
        self.recursers = 0

    def add(self, c):
        self.nrsubdirs += c.nrsubdirs
        self.nrsubwipd += c.nrsubwipd
        self.nroffiles += c.nroffiles
        self.nrfilwipd += c.nrfilwipd
        self.nrofbytes += c.nrofbytes
        self.filwipers += c.filwipers
        self.dirwipers += c.dirwipers
        self.recursers += c.recursers

    def __str__(self):
        return f'''
  nr of subdirs         : {p3.dottify(self.nrsubdirs,15)}
  nr of subdirs wiped   : {p3.dottify(self.nrsubwipd,15)}
  nr of files           : {p3.dottify(self.nroffiles,15)}
  nr of files wiped     : {p3.dottify(self.nrfilwipd,15)}
  nr of bytes freed     : {p3.dottify(self.nrofbytes,15)}
  nr of file wipe fails : {p3.dottify(self.filwipers,15)}
  nr of recurse fails   : {p3.dottify(self.recursers,15)}
  nr of dir wipe fails  : {p3.dottify(self.dirwipers,15)}
'''

sp = {
    r"c:\guivho\_downloads": 7,
    r"c:\guivho\_logs": 7,
    r"c:\guivho\_screenshots": 4,
    r"c:\guivho\_yots": 7,
    r"c:\guivho\appdata\local\temp": 1,
    r"c:\windows\temp": 2,
}

log = p3.Log("wip")

def wipe(p, keepdate, counts):
    md = (datetime.datetime.fromtimestamp(os.path.getmtime(p))).date()
    log.log(f"\n{md} > {p}")
    try:
        items = os.listdir(p)
    except PermissionError as permerr:
        log.log(f"\n{p} => PermissionError")
        counts.recursers += 1
        return counts
    else:
        # recursive wipe all subdirs
        dirs = [item for item in items if os.path.isdir(os.path.join(p,item))]
        for s in dirs:
            counts.nrsubdirs += 1
            wipe(os.path.join(p, s), keepdate, counts)
            # remove any empty subdir
            ps = os.path.join(p, s)
            rest = os.listdir(ps)
            md = (datetime.datetime.fromtimestamp(os.path.getmtime(ps))).date()
            m = '?' if(len(os.listdir(ps)) == 0) else '+'
            exc = ""
            if m == '?':
                try:
                    os.rmdir(ps)
                except Exception as inst:
                    exc = f" ===> {type(inst)}"
                    counts.dirwipers += 1
                if os.path.isdir(ps):
                    m = '!'
                else:
                    counts.nrsubwipd += 1
                    m = '-'
            log.log(f"{md} {m} {ps} {exc}")
        # wipe eligeable files
        files = [item for item in items if os.path.isfile(os.path.join(p,item))]
        for f in files:
            counts.nroffiles += 1
            pf = os.path.join(p, f)
            m = (datetime.datetime.fromtimestamp(os.path.getmtime(pf))).date()
            w = '?' if m < keepdate else '+'
            exc = ""
            if w == '?':
                fs = os.path.getsize(pf)
                try:
                    os.remove(pf)
                except Exception as inst:
                    exc = f" ===> {type(inst)}"
                    counts.filwipers += 1
                if os.path.isfile(pf):
                    w = '!'
                else:
                    counts.nrfilwipd += 1
                    counts.nrofbytes += fs
                    w = '-'
            log.log(f"{m} {w} ..\\{f} {exc}")
        return counts

def main():
    log.log(f"wiper log started at {p3.yso()} {p3.hms()}")
    totals = Counts()
    for p, nrofdays in sp.items():
        keepdate = datetime.date.today() - datetime.timedelta(days = nrofdays)
        log.log(f"\n{p} {nrofdays=} keepdate={keepdate.strftime('%Y-%m-%d')}\n")
        c = wipe(p, keepdate, Counts())
        log.log(f"\n// {p}{c}")
        totals.add(c)
    log.log(f'''
Wiper totals:
{totals}''')

if __name__ == '__main__':
    main()
