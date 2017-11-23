import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
tab=[]
for i in range(height):
    line = input()  # width characters, each either 0 or .
    tab.insert(i,line)

for y in range(height):
    for x in range(width):
        if tab[y][x] != "." :
            abs=x+1
            ord=y
            while abs <= (width-1) and tab[ord][abs] == "." :
                abs+=1
            if abs <= (width-1) :
                x2=abs
                y2=ord
            else:
                x2=-1
                y2=-1
            abs=x
            ord=y+1
            while ord <= (height-1) and tab[ord][abs] == "." :
                ord+=1
            if ord <= (height-1) :
                x3=abs
                y3=ord
            else:
                x3=-1
                y3=-1
            print(x,y,x2,y2,x3,y3)