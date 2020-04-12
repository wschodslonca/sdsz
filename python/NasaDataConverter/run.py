from mapDrawer.drawer import convertToPng
import os
import time


YEAR = 2000

#-180 = W 180 = N

#convertToPng("resources/L3_ozone_omi_20060717.txt","../../src/resources/img/pythonEarth.png")
#convertToPng("resources/L3_ozone_omi_20060717.txt","resources/imgs/imgg.png")

start = time.time()
g = 1
for dirpath, dirnames, filenames in os.walk("resources/data/texts/2000"):
    filenames.sort()
    for i in filenames:
        frompath = os.path.join(dirpath,i)
        topath = f"../../src/resources/img/nasa/{YEAR}/{g}.png"
        try:
            convertToPng(frompath,topath)
        except:
            print("unable to convert")
        g+=1

end = time.time()
print(end-start)