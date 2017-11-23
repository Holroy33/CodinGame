import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
best_diff=9999999999
pi_list=[]
for i in range(n):
    pi = int(input())
    pi_list.insert(i,pi)
pi_list.sort()
i=1
while i < n :
    diff = pi_list[i] - pi_list[i-1]
    if diff < best_diff :
        best_diff = diff
    i+=1
print(best_diff)
# To debug: print("Debug messages...", file=sys.stderr)