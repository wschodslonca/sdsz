class DataScraper:
    def __init__(self, path='', lat=180, long=360):
        self.lat = lat
        self.long = long
        self.path = path
        self.file = None
        self.date = ''
        self.data = None
        if path!='':
            try:
                self.file = open(path,'r')
                self.data = self.file.read()
            finally:
                self.file.close()
            self.setLongLatDate()

    def setDate(self,date):
        try:
            ret=''
            ret += self.monthToNumber(date[0:3])
            if date[4]==' ':
                ret+='0'+date[5]
            else: ret+=date[4:6]
            ret+=date[8:12]
            return ret
        except:
            return "Err#r"

    def setLongLatDate(self):
        #self.file = open(self.path,'r')
        #str = self.file.read()
        self.date = self.setDate(self.data[10:22])
        print(self.date)
        longStart = self.data.find('Longitudes:  ')+13
        self.long = int(self.data[longStart:longStart+3])
        latStart = self.data.find('Latitudes :  ')+13
        self.lat = int(self.data[latStart:latStart+3])
        self.file.close()



    def getDuValues(self):
        def delSpaces(str,step):
            i=0
            res = ""
            lenn = len(str)
            while i<=len(str):
                to = i+step
                if to>lenn:
                    to = lenn
                res+=str[i:i+step]
                i+=step+1
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

        #244 903

        #startIn = str.find('N  (1.00 degree steps)')+26

        start = ind["start"]
        step = 903
        stepStop = 886
        if self.long==288:
            step = ind["step288"]
            stepStop = ind["stepStop288"]
        elif self.long==360:
            step = ind["step360"]
            stepStop = ind["stepStop360"]

        listByLat = []
        test= 1
        for i in range(self.lat):
            values = []
            startIn = start+i*step
            stop = startIn + stepStop
            rawStr = self.data[startIn:stop].replace("\n","")
            rawStr = delSpaces(rawStr,75)
            for j in range(self.long):
                values.append(int(rawStr[j*3:j*3+3].strip()))

            listByLat.append(values)
        listByLat.reverse()
        return listByLat

    def duToRgb(self,j):
        if j==0: # brak danych
            return (128,128,128)
        elif j>0 and j<25:
            return (51,0,25)
        elif j>=25 and j<50:
            return (102,0,51)
        elif j>=50 and j<75:
            return (153,0,153)
        elif j>=75 and j<100:
            return (102,0,204)
        elif j>=100 and j<125:
            return (51,51,255)
        elif j>=125 and j<150:
            return (0,0,204)
        elif j>=150 and j<175:
            return (0,0,102)
        elif j>=175 and j<200:
            return (0,102,204)
        elif j>=200 and j<225:
            return (51,153,255)
        elif j>=225 and j<250:
            return (0,204,204)
        elif j>=250 and j<275:
            return (0,255,255)
        elif j>=275 and j<300:
            return (102,255,255)
        elif j>=300 and j<325:
            return (102,255,102)
        elif j>=325 and j<350:
            return (0,255,0)
        elif j>=350 and j<375:
            return (128,255,0)
        elif j>=375 and j<400:
            return (153,255,51)
        elif j>=400 and j<425:
            return (255,255,51)
        elif j>=425 and j<450:
            return (255,255,0)
        elif j>=450 and j<475:
            return (255,128,0)
        elif j>=475 and j<500:
            return (204,102,0)
        elif j>=500 and j<525:
            return (204,0,0)
        elif j>=525 and j<550:
            return (255,0,0)
        elif j>=550 and j<575:
            return (255,0,50)
        elif j>=575 and j<600:
            return (255,0,127)
        elif j>=600 and j<625:
            return (255,0,255)
        elif j>=625 and j<650:
            return (255,50,255)
        elif j>=650 and j<675:
            return (255,100,255)
        elif j>=675 and j<700:
            return (255,150,255)
        else:
            return (255,255,255)

    def duToRgbList(self,list):
        data = []
        for i in list:
            for j in i:
                data.append(self.duToRgb(j))
        return data

    def nasaDataToRgb(self):
        return self.duToRgbList(self.getDuValues())

    def nasaDataToRgbByValues(self,values):
        return self.duToRgbList(values)

    def monthToNumber(self,month):
        if month=='Jan':
            return '01'
        elif month=='Feb':
            return '02'
        elif month=='Mar':
            return '03'
        elif month=='Apr':
            return '04'
        elif month=='May':
            return '05'
        elif month=='Jun':
            return '06'
        elif month=='Jul':
            return '07'
        elif month=='Aug':
            return '08'
        elif month=='Sep':
            return '09'
        elif month=='Oct':
            return '10'
        elif month=='Nov':
            return '11'
        elif month=='Dec':
            return '12'
        else:
            return '-1'