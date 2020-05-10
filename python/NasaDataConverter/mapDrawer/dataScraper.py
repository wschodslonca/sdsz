class DataScrapper:
    def __init__(self,file):
        self.lat = 180
        self.long = 288
        self.file = file

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

        file = open(self.file,'r')
        str = file.read()
        longStart = str.find('Longitudes:  ')+13
        self.long = int(str[longStart:longStart+3])
        latStart = str.find('Latitudes :  ')+13
        self.lat = int(str[latStart:latStart+3])
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
            rawStr = str[startIn:stop].replace("\n","")
            rawStr = delSpaces(rawStr,75)
            for j in range(self.long):
                values.append(int(rawStr[j*3:j*3+3].strip()))

            listByLat.append(values)
        listByLat.reverse()
        return listByLat

    def duToRgb(self,list):
        data = []
        for i in list:
            for j in i:
                if j==0: # brak danych
                    data.append((128,128,128))
                elif j>0 and j<25:
                    data.append((51,0,25))
                elif j>=25 and j<50:
                    data.append((102,0,51))
                elif j>=50 and j<75:
                    data.append((153,0,153))
                elif j>=75 and j<100:
                    data.append((102,0,204))
                elif j>=100 and j<125:
                    data.append((51,51,255))
                elif j>=125 and j<150:
                    data.append((0,0,204))
                elif j>=150 and j<175:
                    data.append((0,0,102))
                elif j>=175 and j<200:
                    data.append((0,102,204))
                elif j>=200 and j<225:
                    data.append((51,153,255))
                elif j>=225 and j<250:
                    data.append((0,204,204))
                elif j>=250 and j<275:
                    data.append((0,255,255))
                elif j>=275 and j<300:
                    data.append((102,255,255))
                elif j>=300 and j<325:
                    data.append((102,255,102))
                elif j>=325 and j<350:
                    data.append((0,255,0))
                elif j>=350 and j<375:
                    data.append((128,255,0))
                elif j>=375 and j<400:
                    data.append((153,255,51))
                elif j>=400 and j<425:
                    data.append((255,255,51))
                elif j>=425 and j<450:
                    data.append((255,255,0))
                elif j>=450 and j<475:
                    data.append((255,128,0))
                elif j>=475 and j<500:
                    data.append((204,102,0))
                elif j>=500 and j<525:
                    data.append((204,0,0))
                elif j>=525 and j<550:
                    data.append((255,0,0))
                elif j>=550 and j<575:
                    data.append((255,0,50))
                elif j>=575 and j<600:
                    data.append((255,0,127))
                elif j>=600 and j<625:
                    data.append((255,0,255))
                elif j>=625 and j<650:
                    data.append((255,50,255))
                elif j>=650 and j<675:
                    data.append((255,100,255))
                elif j>=675 and j<700:
                    data.append((255,150,255))
                else:
                    data.append((255,255,255))
        return data

    def nasaDataToRgb(self):
        return self.duToRgb(self.getDuValues())