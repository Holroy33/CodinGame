import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()
result=""
count=0
bin_msg=""
for i in range(len(message)):
    char=message[i]
    bin_char=bin(ord(char))[2:]
    if len(str(bin_char)) < 7:
        bin_char="0"+bin_char
    bin_msg=bin_msg+bin_char
debut=""
corps=""
prev_char2=""
for j in range(len(bin_msg)):
    char2=bin_msg[j]
    if j == 0 :
        prev_char2 = char2
        count=1
        if char2 == "1" :
            debut="0"
        else:
            debut="00"
    else:
        if char2 == prev_char2 :
            count+=1
        else:
            for k in range(count) :
                corps=corps + "0"
            if len(result) == 0 :
                result = str(debut) + " " + str(corps)
            else:
                result = result + " " + str(debut) + " " + str(corps)
            prev_char2 = char2                
            count=1
            corps=""
            if char2 == "1" :
                debut="0"
            else:
                debut="00"
for k in range(count) :
    corps=corps + "0"
result = result + " " + str(debut) + " " + str(corps)                
print(result)