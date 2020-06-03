from mapDrawer.datascraper import DataScraper
from PIL import Image
import os

def convertToPng(fileTo, scraper=DataScraper(), listx=None, datax=None,alphax=255):
    scr = scraper
    if datax is not None:
        data = datax
    else:
        if listx is not None:
            data = scr.nasaDataToRgbByValues(listx)
        else:
            data = scr.nasaDataToRgb()
    img = Image.new('RGB', (scr.long, scr.lat))
    img.putdata(data)
    try:
        img.putalpha(alphax)
    except:
        print('failure...')

    bg = None
    if scr.long == 288:
        bg = Image.open(os.path.join(__file__,'..','img/earth288.png'))
    elif scr.long == 360:
        bg = Image.open(os.path.join(__file__,'..','img/earth360.png'))

    bg.paste(img, (0, 0), img)
    bg.save(fileTo)
    print('success!')

def convertToPngByFile(fileFrom,fileTo):
    scraper = DataScraper(fileFrom)
    data = scraper.nasaDataToRgb()
    img = Image.new('RGB',(scraper.long,scraper.lat))
    img.putdata(data)
    try:
        img.putalpha(255)
    except:
        print('failure...')

    bg = None
    if scraper.long==288:
        bg = Image.open("mapDrawer/img/earth288.png")
    elif scraper.long==360:
        bg = Image.open("mapDrawer/img/earth360.png")

    bg.paste(img, (0, 0), img)
    bg.save(fileTo)
    print('success!')
