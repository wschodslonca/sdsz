from sets.func import *
from copy import deepcopy

def color(listx,pixels):
    pattern = deepcopy(listx)
    hei = len(listx)
    wid = len(listx[0])
    currcolor = round(mincolor(listx))
    lowercolor = currcolor-25
    if lowercolor<=0:
        pass
    lowerrgb = dutorgb(lowercolor)
    for i in range(hei):
        for j in range(wid):
            if round(pattern[i][j])==currcolor:
                if j-pixels>=0 and j+pixels<wid and i-pixels>=0 and i+pixels<hei:
                    ifcolor = True
                    for k in range(1,pixels+1):
                        if round(pattern[i-k][j])!=currcolor or round(pattern[i+k][j])!=currcolor or round(pattern[i][j-k])!=currcolor or round(pattern[i][j+k])!=currcolor:
                            ifcolor=False
                    if ifcolor:
                        listx[i][j] = lowercolor





