import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
max = a[0]
min = a[0]

for i in range(n):
    if a[i] <= min:
        min = a[i]
    if a[i] >= max:
        max = a[i]

print(min, max)
