MAXVALUE = 1000


def mincolor(listx):
    min = MAXVALUE
    for i in listx:
        for j in i:
            if j < min and j != 0:
                min = j
    return min


def maxcolor(listx):
    max = 1
    for i in listx:
        for j in i:
            if j > max:
                max = j
    return max


def datetoint(date):
    month = None
    day = None
    year = None
    try:
        month = int(date[0:2])
        day = int(date[2:4])
        year = int(date[4:8])
    except:
        return (-1, -1, -1)
    return (month, day, year)


def dutorgb(j):
    if j == 0:  # brak danych
        return (128, 128, 128)
    elif j > 0 and j < 25:
        return (51, 0, 25)
    elif j >= 25 and j < 50:
        return (102, 0, 51)
    elif j >= 50 and j < 75:
        return (153, 0, 153)
    elif j >= 75 and j < 100:
        return (102, 0, 204)
    elif j >= 100 and j < 125:
        return (51, 51, 255)
    elif j >= 125 and j < 150:
        return (0, 0, 204)
    elif j >= 150 and j < 175:
        return (0, 0, 102)
    elif j >= 175 and j < 200:
        return (0, 102, 204)
    elif j >= 200 and j < 225:
        return (51, 153, 255)
    elif j >= 225 and j < 250:
        return (0, 204, 204)
    elif j >= 250 and j < 275:
        return (0, 255, 255)
    elif j >= 275 and j < 300:
        return (102, 255, 255)
    elif j >= 300 and j < 325:
        return (102, 255, 102)
    elif j >= 325 and j < 350:
        return (0, 255, 0)
    elif j >= 350 and j < 375:
        return (128, 255, 0)
    elif j >= 375 and j < 400:
        return (153, 255, 51)
    elif j >= 400 and j < 425:
        return (255, 255, 51)
    elif j >= 425 and j < 450:
        return (255, 255, 0)
    elif j >= 450 and j < 475:
        return (255, 128, 0)
    elif j >= 475 and j < 500:
        return (204, 102, 0)
    elif j >= 500 and j < 525:
        return (204, 0, 0)
    elif j >= 525 and j < 550:
        return (255, 0, 0)
    elif j >= 550 and j < 575:
        return (255, 0, 50)
    elif j >= 575 and j < 600:
        return (255, 0, 127)
    elif j >= 600 and j < 625:
        return (255, 0, 255)
    elif j >= 625 and j < 650:
        return (255, 50, 255)
    elif j >= 650 and j < 675:
        return (255, 100, 255)
    elif j >= 675 and j < 700:
        return (255, 150, 255)
    else:
        return (255, 255, 255)


def rgbtodu(j):
    if j == (128, 128, 128):  # brak danych
        return 0
    elif j == (51, 0, 25):
        return 20
    elif j == (102, 0, 51):
        return 45
    elif j == (153, 0, 153):
        return 70
    elif j == (102, 0, 204):
        return 95
    elif j == (51, 51, 255):
        return 120
    elif j == (0, 0, 204):
        return 145
    elif j == (0, 0, 102):
        return 170
    elif j == (0, 102, 204):
        return 195
    elif j == (51, 153, 255):
        return 220
    elif j == (0, 204, 204):
        return 245
    elif j == (0, 255, 255):
        return 270
    elif j == (102, 255, 255):
        return 295
    elif j == (102, 255, 102):
        return 320
    elif j == (0, 255, 0):
        return 345
    elif j == (128, 255, 0):
        return 370
    elif j == (153, 255, 51):
        return 395
    elif j == (255, 255, 51):
        return 420
    elif j == (255, 255, 0):
        return 445
    elif j == (255, 128, 0):
        return 470
    elif j == (204, 102, 0):
        return 495
    elif j == (204, 0, 0):
        return 520
    elif j == (255, 0, 0):
        return 545
    elif j == (255, 0, 50):
        return 570
    elif j == (255, 0, 127):
        return 595
    elif j == (255, 0, 255):
        return 620
    elif j == (255, 50, 255):
        return 645
    elif j == (255, 100, 255):
        return 670
    elif j == (255, 150, 255):
        return 695
    else:
        return 0


def rround(j):
    if j == 0:  # brak danych
        return 0
    elif j > 0 and j < 25:
        return 20
    elif j >= 25 and j < 50:
        return 45
    elif j >= 50 and j < 75:
        return 70
    elif j >= 75 and j < 100:
        return 95
    elif j >= 100 and j < 125:
        return 120
    elif j >= 125 and j < 150:
        return 145
    elif j >= 150 and j < 175:
        return 170
    elif j >= 175 and j < 200:
        return 195
    elif j >= 200 and j < 225:
        return 220
    elif j >= 225 and j < 250:
        return 245
    elif j >= 250 and j < 275:
        return 270
    elif j >= 275 and j < 300:
        return 295
    elif j >= 300 and j < 325:
        return 320
    elif j >= 325 and j < 350:
        return 345
    elif j >= 350 and j < 375:
        return 370
    elif j >= 375 and j < 400:
        return 395
    elif j >= 400 and j < 425:
        return 420
    elif j >= 425 and j < 450:
        return 445
    elif j >= 450 and j < 475:
        return 470
    elif j >= 475 and j < 500:
        return 495
    elif j >= 500 and j < 525:
        return 520
    elif j >= 525 and j < 550:
        return 545
    elif j >= 550 and j < 575:
        return 570
    elif j >= 575 and j < 600:
        return 595
    elif j >= 600 and j < 625:
        return 620
    elif j >= 625 and j < 650:
        return 645
    elif j >= 650 and j < 675:
        return 670
    elif j >= 675 and j < 700:
        return 695
    else:
        return 0


def monthtonumber(month):
    if month == 'Jan':
        return '01'
    elif month == 'Feb':
        return '02'
    elif month == 'Mar':
        return '03'
    elif month == 'Apr':
        return '04'
    elif month == 'May':
        return '05'
    elif month == 'Jun':
        return '06'
    elif month == 'Jul':
        return '07'
    elif month == 'Aug':
        return '08'
    elif month == 'Sep':
        return '09'
    elif month == 'Oct':
        return '10'
    elif month == 'Nov':
        return '11'
    elif month == 'Dec':
        return '12'
    else:
        return '-1'


def dutorgblist(list):
    data = []
    for i in list:
        for j in i:
            data.append(dutorgb(j))
    return data


def nasadatatorgbbyvalues(values):
    return dutorgblist(values)


def grabdatabyear(listx, year):
    ant = -1
    arc = -1
    glob = -1
    for i in range(len(listx)):
        for j in range(len(listx[i])):
            if listx[i][j][0] == year:
                if i == 0:
                    ant = listx[i][j][1]
                elif i == 1:
                    arc = listx[i][j][1]
                elif i == 2:
                    glob = listx[i][j][1]
    return ant, arc, glob
