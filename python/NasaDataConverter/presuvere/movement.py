def move(list, arealist,pattern, pixels, color, stfrom=0, endon=180): # arealist - rgb format
    hei = len(arealist)
    wid = len(arealist[0])
    for i in range(stfrom,endon):
        for j in range(wid):
            if arealist[i][j]==color:
                rgbval = arealist[i][j]
                val = pattern[i][j]
                list[i][j]=val
                print(val)
                if i-1>=0:
                    if arealist[i-1][j]!=(255,255,255) or arealist[i-1][j]!=rgbval:
                        for k in range(1,pixels+1):
                            if i-k>=0:
                                list[i-k][j]=val
                if j-1>=0:
                    if arealist[i][j-1]!=(255,255,255) or arealist[i][j-1]!=rgbval:
                        for k in range(1,pixels+1):
                            if j-k>=0:
                                list[i][j-k]=val
                if i+1<hei:
                    if arealist[i+1][j]!=(255,255,255) or arealist[i+1][j]!=rgbval:
                        for k in range(1,pixels+1):
                            if i+k<hei:
                                list[i+k][j]=val
                if j+1<wid:
                    if arealist[i][j+1]!=(255,255,255) or arealist[i][j+1]!=rgbval:
                        for k in range(1,pixels+1):
                            if j+k<wid:
                                list[i][j+k]=val
