from markdrawers.lister import filetolist
import os

MAXVALUE = 1000

def main():
    year = 1985  # base year
    dir = f"../../../src/resources/img/base{year}/data/"

    maxdu = -1
    mindu = MAXVALUE
    for dirpath, dirnames, filenames in os.walk(dir):
        filenames.sort()
        for f in filenames:
            print(f)
            lst = filetolist(dir+f)
            for i in lst:
                for j in i:
                    if j>maxdu:
                        maxdu=j
                        print('new maxdu!: ',maxdu)
                    if j<mindu and j!=0:
                        mindu = j
                        print('new mindu!: ',mindu)

    print(maxdu, mindu) # 604, 124

if __name__=='__main__':
    main()

