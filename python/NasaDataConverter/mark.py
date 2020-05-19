from mapDrawer.datascraper import DataScraper
from areaMarker.areamarker import mark
from mapDrawer.drawer import *
import os
import time

# pathfrom = '../resources/data/texts/2005/L3_ozone_omi_20051018.txt'
# pathto = '../resources/data/test/to/test.png'
# scraper = DataScraper(pathfrom)
# new = mark(scraper)
# convertToPng(scraper,pathto,None,new)

year = int(input("type year to convert: "))

todir = f"../../src/resources/img/sim/{year}/"
fromdir = f"resources/data/texts/{year}/"

if os.path.exists(fromdir):
    if not os.path.exists(todir):
        try:
            os.mkdir(todir)
        except:
            print("unable to create dir")
            exit(-1)
else:
    print(f"no data in year {year}")
    exit(-1)

start = time.time()
g = 1
for dirpath, dirnames, filenames in os.walk(fromdir):
    filenames.sort()
    for i in filenames:
        frompath = os.path.join(dirpath,i)
        print(frompath)
        try:
            scraper = DataScraper(frompath)
            topath = todir+scraper.date+'.png'
            print(topath)
            new = mark(scraper)
            convertToPng(scraper,topath,None,new)
        except:
            print("unable to convert")
        g+=1

end = time.time()
print(end-start)
