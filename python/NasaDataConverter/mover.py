from presuvere.refact import move
from mapDrawer.lister import *
from mapDrawer.drawer import convertToPng
from copy import deepcopy
import time
import os

tempfile = '10241985'
year = 1985
simyear = 2000

dirbase = f"../../src/resources/img/base{year}/"
dir = dirbase+"data/"
dirarea = dirbase+"areadata/"
dirtest = dirbase+"test/"
dirsim = dirbase+f"{simyear}/"
path = dir+tempfile+'.txt'
patharea = dirarea+tempfile+'.txt'
pathtest = dirtest+tempfile+'.png'

if os.path.exists(dirbase):
    if os.path.exists(dir) and os.path.exists(dirarea):
        if not os.path.exists(dirsim):
            os.mkdir(dirsim)
        else:
            print("data already exists")
            exit(0)

pixels = 5
#queue = [(51,153,255),(0,102,204),(0,0,102)]
queue = [(51,153,255),(0,102,204),(0,0,102),(0,0,204),(51,51,255),(102,0,204)]
stfrom = 100

start = time.time()
data = filetoList(path)
pattern = deepcopy(data)
arealist = filetoList(patharea)
for cl in queue:
    print(cl)
    move(data,arealist,pattern.copy(),pixels,cl,stfrom=stfrom)
convertToPng(pathtest, listx=data)
end = time.time()
print(end-start)
