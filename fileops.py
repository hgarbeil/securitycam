import os
import glob
import time
import datetime



def get_file_list():
    # get jpeg files
    list0 = filter(os.path.isfile, glob.glob("assets/*.jpg"))
    jpegs = sorted(list0, key=os.path.getctime)
    jpegs.reverse()
    # get mp4 files
    list1 = filter(os.path.isfile, glob.glob("assets/*.mp4"))
    mp4s = sorted(list1, key=os.path.getmtime)
    mp4s.reverse()
    return (jpegs, mp4s)

def get_file_age (days):
    jpegs=[]
    mp4s=[]
    curtime = curtime = time.time()
    
    list0 = filter(os.path.isfile, glob.glob("assets/*.jpg"))
    list0 = sorted(list0, key=os.path.getctime)
    for f in list0:
        age = (curtime-os.path.getctime(f))/86400.
        if (age > days) :
            continue
        jpegs.append(f)

    list0 = filter(os.path.isfile, glob.glob("assets/*.mp4"))
    list0 = sorted(list0, key=os.path.getctime)
    for f in list0:
        age = (curtime-os.path.getctime(f))/86400.
        if (age > days) :
            continue
        mp4s.append(f)
    return (jpegs,mp4s)
	
	
