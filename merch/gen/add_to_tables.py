import os
os.system('echo Current Path: $PWD')
data1 = raw_input('Enter Unique ID that you want : ')
data2 = raw_input('What do you want the primary storage file to be named : ')
data3 = raw_input('What do you want the secondary storage file to be named? : ')
data4 = "/n"
outF1 = open("tables.txt", "w")
textList1 = [data4, data1, data2, data3]
outF1.close()
outF2 = open("id.txt", "w")
textList2 = [data1]
outF2.close()
