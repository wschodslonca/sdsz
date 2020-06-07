def list1d(list):
    new = []
    for i in list:
        for j in i:
            new.append(j)
    return new


def initempty(h, w):
    empty = []
    for i in range(h):
        empty.append([])
        for j in range(w):
            empty[i].append((255, 255, 255))
    return empty


def move(lat, long, x, y, dir):
    if (dir == 0):
        y -= 1
    elif (dir == 1):
        x += 1
    elif (dir == 2):
        y += 1
    elif (dir == 3):
        x -= 1
    return x, y


def mark(scraper, map=None):
    lat = scraper.lat
    long = scraper.long
    new = initempty(lat, long)
    mapp = None
    if map is None:
        mapp = scraper.getduvalues()
    else:
        mapp = map
    ##### width
    for i in range(lat):
        last = scraper.duToRgb(mapp[i][0])
        for j in range(long):
            val = scraper.duToRgb(mapp[i][j])
            if val != last:
                if j > 0: new[i][j - 1] = last
                new[i][j] = val
                last = val
    ### height
    for j in range(long):
        last = scraper.duToRgb(mapp[0][j])
        for i in range(lat):
            val = scraper.duToRgb(mapp[i][j])
            if val != last:
                if i > 0: new[i - 1][j] = last
                new[i][j] = val
                last = val
    return new
