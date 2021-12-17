import sys

n = int(sys.stdin.readline())

sum = 0

score = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    sum += score[i] / max(score) * 100
print(round((sum / n), 6))
