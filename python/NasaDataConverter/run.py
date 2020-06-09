from simulate import run
import threading

W_INPUT = True

def main(start=1986, end=2020):
    if W_INPUT:
        start = int(input("starting year: "))
        end = int("ending year: ")
    skip = []

    for i in range(start, end + 1, 4):
        t1 = None
        t2 = None
        t3 = None
        t4 = None
        if i >= 1986 and i <= 2020 and i not in skip:
            t1 = threading.Thread(target=run, args=(i,))
            t1.start()
        if i >= 1986 and i <= 2020 and i + 1 not in skip:
            t2 = threading.Thread(target=run, args=(i + 1,))
            t2.start()
        if i >= 1986 and i <= 2020 and i + 2 not in skip:
            t3 = threading.Thread(target=run, args=(i + 2,))
            t3.start()
        if i >= 1986 and i <= 2020 and i + 3 not in skip:
            t4 = threading.Thread(target=run, args=(i + 3,))
            t4.start()
        if t1 is not None:
            t1.join()
        if t2 is not None:
            t1.join()
        if t3 is not None:
            t1.join()
        if t4 is not None:
            t1.join()
