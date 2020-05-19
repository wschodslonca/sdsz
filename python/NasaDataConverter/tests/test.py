from mapDrawer import lister
from mapDrawer.datascraper import DataScraper
import os
import time

YEAR=1980
scraper = None
bef = None
cur = None

g = 0
start = time.time()
for dirpath, dirnames, filenames in os.walk(f"resources/data/texts/{YEAR}"):
    filenames.sort()
    for i in filenames:
        g+=1
        frompath = os.path.join(dirpath, i)
        topath = f"resources/data/test/{YEAR}/{g}.png"
        try:
            if(g==1):
                scraper = DataScraper(frompath)
                bef = scraper.getDuValues()
                continue
            else:
                scraper = DataScraper(frompath)
                cur = scraper.getDuValues()
                for k in range(scraper.lat):
                    for z in range(scraper.long):
                        try:
                            bef[k][z] = cur[k][z]-bef[k][z]
                        except:
                            print("Error")
                lister.listToFile(bef,topath)
                bef.clear()
                bef = cur.copy()
                cur.clear()
                print(g,': success')
        except:
            print(g,': failure')
end = time.time()
print(end-start)