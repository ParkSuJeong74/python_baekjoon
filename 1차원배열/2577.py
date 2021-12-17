import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

tmp = ""
tmp += str(a*b*c)
for i in range(10):
    b = tmp.count("{0}".format(i))
    print(b)
