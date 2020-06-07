from sets.func import *


class DataScraper:
    def __init__(self, path='', lat=180, long=288):
        self.lat = lat
        self.long = long
        self.path = path
        self.file = None
        self.date = ''
        self.data = None
        if path != '':
            try:
                self.file = open(path, 'r')
                self.data = self.file.read()
            finally:
                self.file.close()
            self.setlonglatdate()

    def setdate(self, date):
        try:
            ret = ''
            ret += monthtonumber(date[0:3])
            if date[4] == ' ':
                ret += '0' + date[5]
            else:
                ret += date[4:6]
            ret += date[8:12]
            return ret
        except:
            return "Err#r"

    def setlonglatdate(self):
        self.date = self.setdate(self.data[10:22])
        longStart = self.data.find('Longitudes:  ') + 13
        self.long = int(self.data[longStart:longStart + 3])
        latStart = self.data.find('Latitudes :  ') + 13
        self.lat = int(self.data[latStart:latStart + 3])
        self.file.close()

    def getduvalues(self):
        def delspaces(str, step):
            i = 0
            res = ""
            lenn = len(str)
            while i <= len(str):
                to = i + step
                if to > lenn:
                    to = lenn
                res += str[i:i + step]
                i += step + 1
            return res

        ind = {
            "long": 95,
            "lat": 176,
            "start": 244,
            "stepStop288": 886,
            "step288": 903,
            "stepStop360": 1108,
            "step360": 1125
        }

        # 244 903

        # startIn = str.find('N  (1.00 degree steps)')+26

        start = ind["start"]
        step = 903
        stepStop = 886
        if self.long == 288:
            step = ind["step288"]
            stepStop = ind["stepStop288"]
        elif self.long == 360:
            step = ind["step360"]
            stepStop = ind["stepStop360"]

        listByLat = []
        test = 1
        for i in range(self.lat):
            values = []
            startIn = start + i * step
            stop = startIn + stepStop
            rawStr = self.data[startIn:stop].replace("\n", "")
            rawStr = delspaces(rawStr, 75)
            for j in range(self.long):
                values.append(int(rawStr[j * 3:j * 3 + 3].strip()))

            listByLat.append(values)
        listByLat.reverse()
        return listByLat

    def nasadatatorgb(self):
        return dutorgblist(self.getduvalues())
