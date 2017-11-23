import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
result=-1
print("nb = " + str(n), file=sys.stderr)
if n == 0:
    print("0")
    sys.exit()
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)

    a_t=abs(t)
    if result == -1:
        result=t
        a_result=a_t
    if a_result > a_t:
        result=t
        a_result=a_t
    if a_result == a_t and t > 0 :
        result=t
        a_result=a_t
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(result)