from mapDrawer.dataScraper import DataScraper
from mapDrawer.drawer import convertToPngByList
import os
import time
import random
random.seed()

YEAR = 2005

#scraper = DataScraper('resources/data/texts/2005/L3_ozone_omi_20050101.txt')
scraper = DataScraper('resources/data/test/from/from.txt')
cur = scraper.getDuValues()

next = []


start = time.time()
for days in range(1,365+1):
    for i in range(180):
        next.append([])
        for j in range(360):
            randVal = random.randrange(-2,2)
            sum=0
            for k in range(i-3,i+4):
                for z in range(j-3,j+4):
                    if k!=i or z!=j:
                        if k<0: k=k+180
                        if k>179: k=k-180
                        if z<0: z=z+360
                        if z>359: z=z-360
                        sum+=cur[k][z]
            next[i].append(cur[i][j]+-10)
            #next[i].append(cur[i][j]+random.randrange(-2,2))

    topath = f"../../src/resources/img/sim/{YEAR}/{days}.png"
    convertToPngByList(cur, topath)
    cur.clear()
    cur=next.copy()
    next.clear()

end = time.time()
print(end-start)







