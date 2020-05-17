from mapDrawer.drawer import convertToPng
from mapDrawer.dataScraper import DataScraper
import os
import time


YEAR = 2005

#-180 = W 180 = N

#convertToPng("resources/L3_ozone_omi_20060717.txt","../../src/resources/img/pythonEarth.png")
#convertToPng("resources/L3_ozone_omi_20060717.txt","resources/imgs/imgg.png")

todir = f"../../src/resources/img/nasa/{YEAR}/"

start = time.time()
g = 1
for dirpath, dirnames, filenames in os.walk(f"resources/data/texts/{YEAR}"):
    filenames.sort()
    for i in filenames:
        frompath = os.path.join(dirpath,i)
        try:
            scraper = DataScraper(frompath)
            topath = todir+scraper.date+'.png'
            convertToPng(scraper,topath)
        except:
            print("unable to convert")
        g+=1

end = time.time()
print(end-start)