# Change names to timestamps (YYYYMMDD_HH_MM_SS)
import os, datetime

path = 'testfiles\\'

files2 = os.listdir(path)

for file in files2:
    mtime = os.stat(path + file).st_mtime
    date = datetime.datetime.fromtimestamp(mtime)
    new = (str(date.year)+ str(date.month) + str(date.day) + "_" + str(date.hour) + "_" +
        str(date.minute) + "_" + str(date.second))
    print(file)
    print(mtime)
    print(new, "\n")
    os.rename(path + file, path + new)

