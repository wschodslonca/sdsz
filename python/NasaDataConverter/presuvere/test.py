from presuvere.refact import move
from mapDrawer.lister import *
from mapDrawer.drawer import convertToPng
from copy import deepcopy
import time

tempfile = '10251985'
year = 1985

dir = f"../../../src/resources/img/base{year}/data/"
dirarea = f"../../../src/resources/img/base{year}/areadata/"
dirtest = f"../../../src/resources/img/base{year}/test/"
path = dir+tempfile+'.txt'
patharea = dirarea+tempfile+'.txt'
pathtest = dirtest+tempfile+'.png'

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
