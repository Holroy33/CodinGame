import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]
print("Nodes : "+str(n)+"\t Links : "+str(l)+"\t Exit : "+str(e), file=sys.stderr)
forme=[]
for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    forme.insert(i,(n1,n2,1))
forme.sort()
print("Forme :"+str(forme), file=sys.stderr)

for item in forme:
    if 11 in item:
        print(item)

for i in range(e):
    ei = int(input())  # the index of a gateway node
    print("Exit Index : "+str(ei), file=sys.stderr)
# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    print("Skynet Index : "+str(si), file=sys.stderr)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

