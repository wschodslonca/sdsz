from mapDrawer.dataScraper import DataScraper
from areaMarker.areamarker import mark
from mapDrawer.drawer import *
import os
import time

# pathfrom = '../resources/data/texts/2005/L3_ozone_omi_20051018.txt'
# pathto = '../resources/data/test/to/test.png'
# scraper = DataScraper(pathfrom)
# new = mark(scraper)
# convertToPng(scraper,pathto,None,new)



YEAR = 2005
todir = f"{__file__}/../../../../src/resources/img/sim/{YEAR}/"

start = time.time()
g = 1
for dirpath, dirnames, filenames in os.walk(f"{__file__}/../../resources/data/texts/{YEAR}"):
    filenames.sort()
    for i in filenames:
        frompath = os.path.join(dirpath,i)
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
