import sys
import math
import string

cases = int(sys.stdin.readline().rstrip())

for i in range(cases):
    line = sys.stdin.readline()
    
    newList = line.split(" ")
    
    
    for j in range(len(newList)):
        
        newList[j] = int (newList[j])
        
    newList.sort()
    
    print(newList[(len(newList))-1])
