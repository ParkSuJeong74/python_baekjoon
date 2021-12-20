import sys

n = input()
n = int(n)

for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
