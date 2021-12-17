import sys

b = set([])

for i in range(10):
    a = int(sys.stdin.readline().rstrip())
    b.add(a % 42)
print(len(b))
