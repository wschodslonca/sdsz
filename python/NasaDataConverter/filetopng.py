from markdrawers.drawer import converttopngbyfile


def main():
    FROMPATH = 'resources/data/test/from/from.txt'
    TOPATH = 'resources/data/test/to/'
    converttopngbyfile(FROMPATH, TOPATH)


if __name__ == '__main__':
    main()
