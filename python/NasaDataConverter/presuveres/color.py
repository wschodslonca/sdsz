from sets.func import *
from copy import deepcopy


def color(listx, pixels, limit=0, stfrom=0, endon=180):
    pattern = deepcopy(listx)
    hei = len(listx)
    wid = len(listx[0])
    currcolor = rround(mincolor(listx))
    lowercolor = currcolor - 25
    if lowercolor < limit:
        return 4  # reached the limit
        pass
    for i in range(stfrom, endon):
        for j in range(wid):
            if rround(pattern[i][j]) == currcolor:
                if j - pixels >= 0 and j + pixels < wid and i - pixels >= 0 and i + pixels < hei:
                    ifcolor = True
                    for k in range(1, pixels + 1):
                        if rround(pattern[i - k][j]) != currcolor or rround(pattern[i + k][j]) != currcolor or rround(
                                pattern[i][j - k]) != currcolor or rround(pattern[i][j + k]) != currcolor:
                            ifcolor = False
                    if ifcolor:
                        listx[i][j] = lowercolor
    return 0


def delthebiggest(listx, limit=0):
    hei = len(listx)
    wid = len(listx[0])
    currcolor = rround(maxcolor(listx))
    lowercolor = currcolor - 25
    if lowercolor <= limit:
        return 4  # reached the limit
    for i in range(hei):
        for j in range(wid):
            if rround(listx[i][j]) == currcolor:
                listx[i][j] = lowercolor

    return 0
