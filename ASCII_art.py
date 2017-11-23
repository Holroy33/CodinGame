import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
t = t.upper()
#print(" Valeur de l : "+str(l),file=sys.stderr)
#print(" Valeur de h : "+str(h),file=sys.stderr)
#print(" Valeur de t : "+str(t),file=sys.stderr)
result=""
for i in range(h):
    row = input()
    ind=0
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
    while ind < len(t):
        char=t[ind]
        if ord(char) < ord("A") or ord(char) > ord("Z"):
            char="["
        offset=ord(char)-ord("A")
        debut=offset*l
        fin=debut+l
        result = result + row[debut:fin]
        ind +=1
    result = result + "\n"
print(result)