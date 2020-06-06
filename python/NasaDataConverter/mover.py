from presuvere.refact import move
from mapDrawer.lister import *
from mapDrawer.drawer import convertToPng
from copy import deepcopy
import time
import os
from set.func import *

simyear = 2000 # year to simulate
pixels = 5 # pixels to move
queue = [(51,153,255),(0,102,204),(0,0,102),(0,0,204),(51,51,255),(102,0,204)] # colors to consider while moving
stfrom = 100 # starting lattitide
narrowdate = False # if you want to start with exact date and date on exact date
startdate = '08131985' # if narrow = True - starting date
enddate = '08231985' # if narrow = True - ending date

year = 1985
godate = True
tupstartdate = None
tupenddate = None
interupt = False
dirbase = f"../../src/resources/img/base{year}/"
dir = dirbase+"data/"
dirarea = dirbase+"areadata/"
dirtest = dirbase+"test/"
dirsim = dirbase+f"{simyear}/"

if os.path.exists(dirbase):
    if os.path.exists(dir) and os.path.exists(dirarea):
        if not os.path.exists(dirsim):
            os.mkdir(dirsim)

if narrowdate:
    godate=False
    tupstartdate = dateToInt(startdate)
    tupenddate = dateToInt(enddate)


start = time.time()
for dirpath, dirnames, filenames in os.walk(dir):
    filenames.sort()
    for i in filenames:
        i = i[0:8]
        if narrowdate:
            tupi = dateToInt(i)
            if not godate:
                if tupi[0]>=tupstartdate[0] and tupi[1]>=tupstartdate[1]:
                    godate=True
            else:
                if tupi[0]>=tupenddate[0] and tupi[1]>=tupenddate[1]:
                    godate=False
                    interupt=True
        if godate:
            path = dir + i + '.txt'
            patharea = dirarea + i + '.txt'
            pathsim = dirsim + i + '.png'
            data = filetoList(path)
            pattern = deepcopy(data)
            arealist = filetoList(patharea)
            for cl in queue:
                print(cl)
                move(data, arealist, pattern.copy(), pixels, cl, stfrom=stfrom)
            convertToPng(pathsim, listx=data)
            if interupt:
                break

end = time.time()
print(end-start)
