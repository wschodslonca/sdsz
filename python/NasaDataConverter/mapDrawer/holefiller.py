import os
from mapDrawer.lister import *
from mapDrawer.drawer import *
from mapDrawer.datascraper import DataScraper


def holefiller(year):
    todir = f"../../src/resources/img/base{year}/"
    print(todir)
    fromdir = f"resources/data/texts/{year}/"
    fromdirprev = f"resources/data/texts/{year-1}/"

    if os.path.exists(fromdir):
        if not os.path.exists(todir):
            try:
                os.mkdir(todir)
                os.mkdir(todir+'/imgs/')
                os.mkdir(todir+'/data/')
            except:
                print("unable to create dir")
                exit(-1)
    else:
        print(f"no data in year {year}")
        exit(-1)

    if os.path.exists(fromdirprev):
        print("prev dir exists")
    else:
        print("there is no previous year...")
        exit(-1)

    #prev
    listx = []
    for dirpath, dirnames, filenames in os.walk(fromdirprev):
        filenames.sort()
        lenf = len(filenames)
        for i in range(lenf-5,lenf):
            listx.append(os.path.join(dirpath, filenames[i]))

    start = 5

    for dirpath, dirnames, filenames in os.walk(fromdir):
        filenames.sort()
        for i in filenames:
            listx.append(os.path.join(dirpath, i))

    biglist =[]
    for i in listx:
        scr = DataScraper(i)
        biglist.append(scr.getDuValues())

    for i in range(start,len(biglist)):
        scr = DataScraper(listx[i])
        map = biglist[i]
        for x in range(scr.lat):
            nonzero = 0
            cont = True
            for z in range(len(biglist[i][x])):
                if map[x][z]!=0:
                    nonzero+=1
                if nonzero>10:
                    cont = False
                    break
            if cont:
                continue
            #changes = len(biglist[i][x])
            for y in range(scr.long):
                tries = 0
                while(map[x][y]==0 and tries<=5):
                    tries += 1
                    prevmap = biglist[i-tries]
                    map[x][y] = prevmap[x][y]
                    #changes-=1
            # if changes<20:
            #     map[x] = pasek
            #     print(map[x])
        try:
            fileto = todir+'imgs/'+scr.date+'.png'
            print(fileto)
            listo = todir+'data/'+scr.date+'.txt'
            print(listo)
            listToFile(map,listo)
            convertToPng(scr,fileto,map)
        except:
            print(f"{i}: holefiller error")








