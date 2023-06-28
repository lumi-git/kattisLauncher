import sys
import sys

line = sys.stdin.read().splitlines()

ti = int(lines[0].split()[1])

li = list(map(int,line[1].split()))


currSum = 0
for i,t in enumerate(li) :
    currSum += t
    if currSum > ti :
        print(i)
        exit()

print(i)