# add saving to CSV
# displaying data in HTML as a charts; LoC(time)
# modifying how often the changes are checked

import os
import time
from languages import lang
from collections import defaultdict

SLEEP_TIME=15 #seconds

def get_date():
    return time.strftime(" %d.%m.%Y, %H:%M ")

def get_path():
    return os.getcwd()

def get_flang(file):
    ext=file.split('.')[-1]
    return lang.get(ext)

def get_lines(file, flang):
    loc=0
    with open(file, encoding="ibm437") as f:
        data=f.read()
    for line in data.splitlines():
        if line.strip()=="":
            continue
        elif flang=="Python":
            if line.strip()=="#":
                continue
            else:
                loc+=1
        elif flang=="C/C++":
            if line.strip()=="//":
                continue
            else:
                loc+=1
        else:
            loc+=1
    return(loc)

def loc_counter_prog():
    path=get_path()
    total_loc=0
    stats=defaultdict(int)
    for root, dirs, files in os.walk(path):
        for i in range (0, len(files)):
           loc=0
           flang=get_flang(files[i])
           fpath=root+"\\"+files[i]
           if flang:
                loc=get_lines(fpath,flang)
                total_loc+=loc
                stats[flang]+=loc
    print({
        "date":get_date(),
        "stats":dict(stats),
        "total":total_loc
        })

while True:
    loc_counter_prog()
    print("Counting...")
    time.sleep(SLEEP_TIME)