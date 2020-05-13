from mapDrawer.dataScraper import DataScraper
from PIL import Image

ALPHA = 255

def convertToPng(fileFrom,fileTo):
    scraper = DataScraper(fileFrom)
    data = scraper.nasaDataToRgb()
    img = Image.new('RGB',(scraper.long,scraper.lat))
    img.putdata(data)
    try:
        img.putalpha(ALPHA)
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

def convertToPngByList(l,fileTo):
    scraper = DataScraper()
    data = scraper.nasaDataToRgbByValues(l)
    img = Image.new('RGB', (scraper.long, scraper.lat))
    img.putdata(data)
    try:
        img.putalpha(ALPHA)
    except:
        print('failure...')

    bg = None
    if scraper.long == 288:
        bg = Image.open("mapDrawer/img/earth288.png")
    elif scraper.long == 360:
        bg = Image.open("mapDrawer/img/earth360.png")

    bg.paste(img, (0, 0), img)
    bg.save(fileTo)
    print('success!')

