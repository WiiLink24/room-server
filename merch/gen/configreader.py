import sys
argdata1 = sys.argv[1] #Line Number
argdata2 = sys.argv[2] #File
file = open(argdata2)
all_lines = file.readlines()
print(all_lines[argdata1])
