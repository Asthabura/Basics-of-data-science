import numpy as np
print("Print all the dates in given month")
print(np.arange('2020-01','2020-02',dtype='datetime64[D]'))
print("Count the No. of days ")
print((np.datetime64('2020-03-01'))-(np.datetime64('2020-02-05')))
print("today's date")
print(np.datetime64('today','D'))
print("yesterday's date")
print((np.datetime64('today','D'))-(np.timedelta64(1,'D')))
print("tomorrow's date")
print((np.datetime64('today','D'))+(np.timedelta64(1,'D')))
