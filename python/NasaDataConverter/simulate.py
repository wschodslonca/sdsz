from presuveres.presuve import move
from presuveres.color import color, delthebiggest
from markdrawers.lister import *
from markdrawers.drawer import converttopng
from copy import deepcopy
import time
import os
from sets.func import *


def main():
    # consts
    BASELOW = 145  # 124
    BASEUP = 595  # 604
    LIMITVAL = 4  # value informating that limit is reached
    COLORUPLIMIT = 520
    COLORDOWNLIMIT = 95

    # info init
    concdata = filetolist('resources/data/ozone_concentration_data.txt')
    simyear = 2020  # year to simulate
    ant, arc, glob = grabdatabyear(concdata, simyear)

    colorup = int(arc / 3)
    pixels = int(ant / 7)
    colordown = int(ant / 25)

    queuedownstart = 245
    queuedownend = 70
    queueupstart = 595
    queueupend = 420
    # queue = [220, (0, 102, 204), (0, 0, 102), (0, 0, 204), (51, 51, 255),
    #        (102, 0, 204)]  # colors to consider while moving
    # [(51, 153, 255), (0, 102, 204), (0, 0, 102), (0, 0, 204), (51, 51, 255),
    #              (102, 0, 204)]
    stfromdown = 140  # starting lattitide
    endonup = 70

    narrowdate = False  # if you want to start with exact date and date on exact date
    startdate = '05241985'  # if narrow = True - starting date
    enddate = '12011985'  # if narrow = True - ending date

    year = 1985
    godate = True
    tupstartdate = None
    tupenddate = None
    interupt = False
    dirbase = f"../../src/resources/img/base{year}/"
    dir = dirbase + "data/"
    dirarea = dirbase + "areadata/"
    dirtest = dirbase + "test/"
    dirsim = dirbase + f"{simyear}/"

    if os.path.exists(dirbase):
        if os.path.exists(dir) and os.path.exists(dirarea):
            if not os.path.exists(dirsim):
                os.mkdir(dirsim)

    if narrowdate:
        godate = False
        tupstartdate = datetoint(startdate)
        tupenddate = datetoint(enddate)

    start = time.time()
    for dirpath, dirnames, filenames in os.walk(dir):
        filenames.sort()
        for f in filenames:
            f = f[0:8]
            if narrowdate:
                tupi = datetoint(f)
                if not godate:
                    if tupi[0] >= tupstartdate[0] and tupi[1] >= tupstartdate[1]:
                        godate = True
                else:
                    if tupi[0] >= tupenddate[0] and tupi[1] >= tupenddate[1]:
                        interupt = True
            if godate:
                print(f)
                path = dir + f + '.txt'
                patharea = dirarea + f + '.txt'
                pathsim = dirsim + f + '.png'
                data = filetolist(path)
                pattern = deepcopy(data)
                arealist = filetolist(patharea)

                # antarctic
                for cl in range(queuedownstart, queuedownend - 1, -25):
                    move(data, pattern, cl, pixels, arealist, stfromdown, 180)
                for i in range(colordown):
                    inf = color(data, 3, COLORDOWNLIMIT, stfrom=stfromdown, endon=180)
                    if inf == LIMITVAL:
                        break

                # arctic
                for i in range(colorup):
                    inf = delthebiggest(data, limit=COLORUPLIMIT)
                    if inf == LIMITVAL:
                        break
                for clr in range(queueupstart, queueupend-1, -25):
                    for i in range(pixels):
                        move(data, pattern, clr, pixels=-1, stfrom=0, endon=endonup)
                        pattern = deepcopy(data)

                # convertion
                converttopng(pathsim, listx=data)
                if interupt:
                    break

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
