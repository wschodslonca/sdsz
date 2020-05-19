from mapDrawer.holefiller import holefiller
import time

start =time.time()

year = int(input("select year: "))
holefiller(year)

end=time.time()
print(end-start)