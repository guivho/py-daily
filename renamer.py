# Time-stamp: <2026-01-06 19:14:39 renamer.py Guivho>

import datetime
import os
import re
import time
import p3

ZERO = "_00"
ROOT = r"c:\Users\guivho\onedrive"
HOME = os.path.join(ROOT, ZERO)
DOWN = r"c:\guivho\_Downloads"
SHOT = r"c:\guivho\_Screenshots"

SCANDIRS = (
DOWN,
HOME,
ROOT,
)

regexes = [
    re.compile(r"Scan - (\d\d\d\d)-(\d\d)-(\d\d) (\d\d)_(\d\d)_(\d\d).(.*)"),
    re.compile(r"kasticket_\d+_(\d\d)-(\d\d)-(\d\d\d\d) (\d\d)-(\d\d).(.*)"),
    re.compile(r"Sc([hr]).*(\d{4})\-?(\d{2})\-?(\d{2})[\- ](\d{6})\.(png.*)"),
]

dest = [
    HOME,
    HOME,
    SHOT,
]

def inspect(log, dir, descend = False, ri = 0):
    names = os.listdir(dir)
    if(descend):
        dirs = [item for item in names if os.path.isdir(os.path.join(dir,item))]
        for sub in dirs:
            inspect(log, os.path.join(dir, sub), descend, ri)
    files = [item for item in names if os.path.isfile(os.path.join(dir,item))]
    for f in files:
        m = regexes[ri].fullmatch(f)
        if m:
            g = m.groups()
            match ri:
                case 0:
                    to = f"{g[0]}{g[1]}{g[2]} {g[3]}{g[4]}{g[5]} scn.{g[6]}"
                case 1:
                    to = f"{g[2]}{g[1]}{g[0]} {g[3]}{g[4]} tck.{g[5]}"
                case _:
                    to = f"{g[1]}{g[2]}{g[3]} {g[4]} {g[0]}.{g[5]}"
            log.log(f"{os.path.join(dir, f)} \n\t\t {os.path.join(dest[ri], to)}\n")
            os.rename(os.path.join(dir, f), os.path.join(dest[ri], to))

def main():
    log = p3.Log("ren")
    descend = not log.exists()
    if descend:
        log.log(f"{ROOT} New log and full recursion!")
        inspect(log, ROOT, descend)
    else:
        for dir in SCANDIRS:
            inspect(log, dir, descend = False, ri = 0)
    inspect(log, dir = DOWN, descend = False, ri = 1)
    inspect(log, dir = SHOT, descend = False, ri = 2)
    log.touch()

if __name__ == '__main__':
    main()
