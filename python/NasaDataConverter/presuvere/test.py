from presuvere.movement import move
from mapDrawer.lister import *
from mapDrawer.drawer import convertToPng
from copy import deepcopy

tempfile = '10041985'
year = 1985

dir = f"../../../src/resources/img/base{year}/data/"
dirarea = f"../../../src/resources/img/base{year}/areadata/"
dirtest = f"../../../src/resources/img/base{year}/test/"
path = dir+tempfile+'.txt'
patharea = dirarea+tempfile+'.txt'
pathtest = dirtest+tempfile+'.png'


#queue = [(51,153,255),(0,102,204),(0,0,102)]
queue = [(51,153,255),(0,102,204),(0,0,102)]

data = filetoList(path)
pattern = deepcopy(data)
arealist = filetoList(patharea)
for cl in queue:
    print(cl)
    move(data,arealist,pattern.copy(),20,cl,stfrom=90)
convertToPng(pathtest, listx=data)
