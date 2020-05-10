from mapDrawer.dataScraper import DataScrapper
from PIL import Image

def convertToPng(fileFrom,fileTo):
    scrapper = DataScrapper(fileFrom)
    #scrapper = DataScrapper('resources/L3_ozone_n7t_19900110.txt')
    data = scrapper.nasaDataToRgb()
    img = Image.new('RGB',(scrapper.long,scrapper.lat))
    img.putdata(data)
    try:
        img.putalpha(230)
        img.save('obr.png','PNG')

        print('success!')
    except:
        print('failure...')

    bg = None
    if scrapper.long==288:
        bg = Image.open("mapDrawer/img/earth288.png")
    elif scrapper.long==360:
        bg = Image.open("mapDrawer/img/earth360.png")

    bg.paste(img, (0, 0), img)
    bg.save(fileTo)
