import sys
argdata = sys.argv[1]
file = open('tables.txt')
all_lines = file.readlines()
print(all_lines[argdata])
fp.close()
