import sys

max = 0
tmp = list()

for i in range(9):
    a = int(sys.stdin.readline())
    tmp.append(a)

    if tmp[i] >= max:
        max = tmp[i]
        index = i+1

print(max)
print(index)
