from markdrawers.drawer import converttopng
from markdrawers.datascraper import DataScraper
import os
import time


def main(year=None):
    if year is None:
        year = int(input("type year to convert: "))

    todir = f"../../src/resources/img/nasa/{year}/"
    fromdir = f"resources/data/texts/{year}/"

    if os.path.exists(fromdir):
        if not os.path.exists(todir):
            try:
                os.mkdir(todir)
            except:
                print("unable to create dir")
                exit(-1)
    else:
        print(f"no data in year {year}")
        exit(-1)

    start = time.time()
    g = 1
    for dirpath, dirnames, filenames in os.walk(f"resources/data/texts/{year}"):
        filenames.sort()
        for i in filenames:
            frompath = os.path.join(dirpath, i)
            try:
                scraper = DataScraper(frompath)
                topath = todir + scraper.date + '.png'
                converttopng(topath, scraper)
            except:
                print("unable to convert")
            g += 1

    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
