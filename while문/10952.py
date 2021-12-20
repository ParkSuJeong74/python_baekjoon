import sys

a, b = map(int, sys.stdin.readline().split())
temp = list()
temp.append(a+b)

while a != 0 and b != 0:
    a, b = map(int, sys.stdin.readline().split())
    temp.append(a+b)

for i in range(len(temp)-1):
    print(temp[i])
