import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ext_dict= {}
fname=""
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext_dict[ext.lower()]=mt
for i in range(q):
    fname = input()  # One file name per line.
    fname=fname.lower()
    if "." not in fname :
        extension=""
    else:
        extension=fname.split('.')[-1]
    if extension in ext_dict.keys():
        print(ext_dict[extension])
    else:
        print("UNKNOWN")
# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
