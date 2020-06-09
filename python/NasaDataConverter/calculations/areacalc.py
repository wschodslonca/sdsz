from markdrawers.lister import listtofile


sourcedir = f"../resources/stratospheric-ozone-concentration-projections.csv"


def main():
    temp = [[], [], []]
    with open(sourcedir) as file:
        file.readline()  # skip of first line
        for i in file:
            g = 0
            ind = -1
            while (i[g] != ','): g += 1
            if i[0:g] == 'Antarctic':
                ind = 0  # antarctic
            elif i[0:g] == 'Arctic':
                ind = 1  # arctic
            elif i[0:g] == 'Global':
                ind = 2  # global

            g += 2
            year = int(i[g:g + 4])
            if year < 1985 or year > 2020: ##############
                continue
            value = float(i[g + 5:len(i)])
            temp[ind].append([year, value])

    for i in range(len(temp)):
        for j in range(len(temp[i])):
            if i == 0:
                temp[i][j][1] += 66.5  # value of 1960
                temp[i][j][1] = round(temp[i][j][1], 1)
            elif i == 1:
                temp[i][j][1] += 12.2  # value of 1960
                temp[i][j][1] = round(temp[i][j][1], 1)
            elif i == 2:
                temp[i][j][1] += 8.3  # value of 1960
                temp[i][j][1] = round(temp[i][j][1], 1)

    data = [[], [], []]

    for i in range(len(temp)):
        lenn = len(temp[i])
        for j in range(lenn):
            year = temp[i][j][0]
            currval = temp[i][j][1]
            data[i].append([year, -1*round(currval,1)+0])
            if j < lenn - 1:
                nextval = temp[i][j + 1][1]
                step = (nextval - currval) / 5
                for k in range(1, 5):
                    data[i].append([year + k, -1*round((currval + step * k), 1)+0])

    listtofile(data,'../resources/data/ozone_concentration_data.txt')


if __name__ == '__main__':
    main()
