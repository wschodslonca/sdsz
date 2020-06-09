from sets.func import *

def move(listx, pattern, color, pixels=0,arealist=None,stfrom=0, endon=180):
    if pixels>0:
        moveup(listx, pattern, color, pixels, arealist,  stfrom, endon)
    elif pixels<0:
        movedown(listx, pattern, color , stfrom=stfrom,endon=endon)

def movedown(listx, pattern, color, stfrom, endon):
    hei = len(listx)
    wid = len(listx[0])
    approcolor = rround(color)
    for i in range(stfrom,endon):
        for j in range(wid):
            if rround(pattern[i][j]) == approcolor:
                clrchange = approcolor
                for d in range(4): # 4 directions
                    ti = i
                    tj = j
                    if d==0:
                        tj-=1
                    elif d==1:
                        ti-=1
                    elif d==2:
                        if tj+1>wid:
                            tj=0
                        else:
                            tj+=1
                    else:
                        if ti+1>hei:
                            ti=0
                        else:
                            ti+=1
                    if ti>=0 and ti<hei and tj>=0 and tj<wid:
                        compcolor = pattern[ti][tj]
                        if compcolor<approcolor and compcolor!=0:
                            clrchange = compcolor
                listx[i][j] = clrchange


def moveup(listx, pattern, color, pixels, arealist, stfrom, endon):  # arealist - rgb format
    hei = len(arealist)
    wid = len(arealist[0])
    for i in range(stfrom, endon):
        for j in range(wid):
            if rround(pattern[i][j]) == rround(color):
                listx[i][j] = pattern[i][j]
            if arealist[i][j] == dutorgb(color):
                rgbval = arealist[i][j]
                val = pattern[i][j]
                listx[i][j] = val
                neibour = [False, False, False, False]  # [0 - up, 1- right, 2 - down, 3 - left]
                if i - 1 >= 0:  # up
                    if arealist[i - 1][j] != (255, 255, 255) and arealist[i - 1][j] != rgbval:
                        neibour[0] = True
                        for k in range(1, pixels + 1):
                            if i - k >= 0:
                                if listx[i - k][j] != 0:
                                    listx[i - k][j] = val
                if j + 1 < wid:  # right
                    if arealist[i][j + 1] != (255, 255, 255) and arealist[i][j + 1] != rgbval:
                        neibour[1] = True
                        for k in range(1, pixels + 1):
                            if j + k < wid:
                                if listx[i][j + k] != 0:
                                    listx[i][j + k] = val
                if i + 1 < hei:  # down
                    if arealist[i + 1][j] != (255, 255, 255) and arealist[i + 1][j] != rgbval:
                        neibour[2] = True
                        for k in range(1, pixels + 1):
                            if i + k < hei:
                                if listx[i + k][j] != 0:
                                    listx[i + k][j] = val
                if j - 1 >= 0:  # left
                    if arealist[i][j - 1] != (255, 255, 255) and arealist[i][j - 1] != rgbval:
                        neibour[3] = True
                        for k in range(1, pixels + 1):
                            if j - k >= 0:
                                if listx[i][j - k] != 0:
                                    listx[i][j - k] = val

                automatacorrect(j, i, listx, neibour, pixels, val)


def automatacorrect(x, y, listx, neib, size,
                    val):  # RULE 0 - upleft , RULE 1 - upright, RULE 2 - downright, RULE 3 - downleft
    hei = len(listx)
    wid = len(listx[0])
    queue = []
    if neib[0] and neib[3]:
        queue.append(0)
    if neib[0] and neib[1]:
        queue.append(1)
    if neib[2] and neib[1]:
        queue.append(2)
    if neib[2] and neib[3]:
        queue.append(3)
    for k in queue:
        i = y
        j = x
        stepi = 0
        stepj = 0
        if k == 0:
            stepi = -1
            stepj = -1
        elif k == 1:
            stepi = -1
            stepj = 1
        elif k == 2:
            stepi = 1
            stepj = 1
        elif k == 3:
            stepi = 1
            stepj = -1
        for z in range(1, int(size / 3) + 1):
            i = i + stepi
            j = j + stepj
            if i >= 0 and i < hei and j >= 0 and j < wid:
                if listx[i][j] != 0:
                    listx[i][j] = val
                tempi = i
                tempj = j
                for g in range(1, ((size - z * 3) + 1)):
                    tempi = tempi + stepi
                    if tempi >= 0 and tempi < hei:
                        if listx[tempi][tempj] != 0:
                            listx[tempi][tempj] = val
                tempi = i
                for g in range(1, ((size - z * 3) + 1)):
                    tempj = tempj + stepj
                    if tempj >= 0 and tempj < wid:
                        if listx[tempi][tempj] != 0:
                            listx[tempi][tempj] = val
