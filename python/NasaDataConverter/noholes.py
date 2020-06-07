from markdrawers.holefiller import holefiller
import time


def main():
    start = time.time()
    year = int(input("select year: "))
    holefiller(year)
    end = time.time()
    print(end - start)


if __name__ == '__main__':
    main()
