from mapDrawer.datascraper import DataScraper
import os

YEAR = 2005

scraper = DataScraper()

days = []

for dirpath, dirnames, filenames in os.walk(f"resources/data/texts/{YEAR}"):
    filenames.sort()
    for i in filenames:
        try:
            scraper.path = os.path.join(dirpath, i)
            days.append(scraper.getDuValues())
        except:
            print("failure")

day1 = days[0]
day2 = days[1]
day3 = days[2]

min = 1000
minij = None
maxij = None
max = -1000

polecenie = 2
if polecenie ==1: # zmiany z dnia 1 na 2
    for i in range(len(day1)):
        for j in range(len(day1[0])):
            d1val = day1[i][j]
            d2val = day2[i][j]
            if d1val!=0 and d2val!=0:
                val = d2val - d1val
                if val<min:
                    min=val
                    minij=(i,j)
                if val>max:
                    max=val
                    maxij=(i,j)
            else:
                val = 'NULL'
            print(f"[({i}, {j}): {val}]",end='',sep=' ')


        print()
    print(minij,': ',min,' | ',maxij,':', max,sep='')
elif polecenie==2: # zmiany w komorce 89,179
    for i in range(len(days)-1):
        val = days[i+1][89][179]-days[i][89][179]
        if days[i + 1][89][179] != 0 and days[i][89][179] != 0:
            if val < min:
                min = val
            if val > max:
                max = val
        else:
            val='NULL'
        print(i+1,'-',i+2,': ',val,sep='')
    print(min,max)





