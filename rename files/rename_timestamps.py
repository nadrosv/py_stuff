# Change names to timestamps (YYYY-MM-DD_HH-MM-SS)
import os, datetime

path = 'testfiles\\'

files2 = os.listdir(path)

for file in files2:
    mtime = os.stat(path + file).st_mtime
    date = datetime.datetime.fromtimestamp(mtime)
    new = str(date)[0:19].replace(':','-',2).replace(' ','_',1)
    print(file)
    print(mtime)
    print(date)
    print(new, '\n')
    
    # os.rename(path + file, path + new)