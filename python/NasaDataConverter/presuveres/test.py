from presuveres.presuve import move
from presuveres.color import color
from markdrawers.lister import *
from markdrawers.drawer import converttopng
from copy import deepcopy
import time


def main():
    tempfile = '10231985'
    year = 1985

    dir = f"../../../src/resources/img/base{year}/data/"
    dirarea = f"../../../src/resources/img/base{year}/areadata/"
    dirtest = f"../../../src/resources/img/base{year}/test/"
    path = dir + tempfile + '.txt'
    patharea = dirarea + tempfile + '.txt'
    pathtest = dirtest + tempfile + '.png'
    pathtestcolor = dirtest + tempfile + 'clr' + '.png'

    pixels = 6
    # queue = [(51,153,255),(0,102,204),(0,0,102)]
    queue = [(51, 153, 255), (0, 102, 204), (0, 0, 102), (0, 0, 204), (51, 51, 255), (102, 0, 204)]
    stfromdown = 100
    endonup = 60

    start = time.time()
    data = filetolist(path)
    pattern = deepcopy(data)
    arealist = filetolist(patharea)
    for cl in queue:
        print(cl)
        move(data, arealist, pattern.copy(), pixels, cl, stfrom=stfromdown)
    converttopng(pathtest, listx=data)

    # tests
    print('--------------\n')
    color(data, 5)
    print('\n---------------\n')

    converttopng(pathtestcolor, listx=data)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
