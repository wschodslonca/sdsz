CFCtab = [1070, 1110, 1080, 1040, 1100, 1090, 1150, 1180, 1280, 1360, 1460, 1410, 1320, 1190, 1080, 960, 820, 760, 700,
          640, 600, 590, 560, 530, 490]


def cfc(year):
    CFC = 2000
    if (year <= 2002):
        i = 0
        while i <= year - 1978:
            CFC -= 600
            CFC += CFCtab[i]
            i += 1
        return CFC
    else:
        i = 0
        while i <= 24:
            CFC -= 600
            CFC += CFCtab[i]
            i += 1
        j = 1
        while j <= year - 2002:
            CFC -= 600
            CFC += CFCtab[24] - (10 * j)
            j += 1
            if CFC <= 200:
                CFC = 200
                break
        return CFC
