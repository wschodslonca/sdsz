from areaMarker.areamarker import mark
from mapDrawer.drawer import *
from mapDrawer.lister import *
from mapDrawer.datascraper import DataScraper
import os
import time

year = int(input("type year to convert: "))

todir = f"../../src/resources/img/base{year}/"
todirarea = f"../../src/resources/img/base{year}/area/"
fromdir = f"../../src/resources/img/base{year}/data/"

if os.path.exists(fromdir):
    if not os.path.exists(todir):
        print(f"no base{year} dir detected")
        exit(-1)
    else:
        if not os.path.exists(todirarea):
            try:
                os.mkdir(todirarea)
            except:
                print(f"unable to create area of {year} dir")
                exit(-1)
else:
    print(f"no data in year {year}")
    exit(-1)

start = time.time()

bigdata =[]
names = []
for dirpath, dirnames, filenames in os.walk(fromdir):
    filenames.sort()
    for i in filenames:
        bigdata.append((i[0:-4],filetoList(os.path.join(dirpath,i)))) # i[0:-4] - filename

scraper = DataScraper()
scraper.lat = len((bigdata[0][1]))
scraper.long = len(bigdata[0][1][0])

for i in bigdata:
    try:
        topath = todirarea+i[0]+'.png'
        new = mark(scraper,i[1])
        convertToPng(scraper,topath,None,new)
    except:
        print("unable to convert")

end = time.time()
print(end-start)
