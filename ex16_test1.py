# import sys
#
#
# filename = sys.argv[1]
# with open(filename, 'r') as f:
#     txt = f.read()
#
#
# print(txt)


import sys

filename = sys.argv[1]

fd = open(filename, "r")

print(fd.read())

fd.close()
