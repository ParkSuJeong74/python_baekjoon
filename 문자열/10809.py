import sys

s = list(str(sys.stdin.readline().split()))
alpa = range(97, 123)
list(alpa)
alpa = [chr(i) for i in alpa]

index = 0
for i in alpa:
    for j in s:
        if i == j:
            index = s.index(j)
            # print(index)
    if index != 0:
        print(index-2, end=" ")
    else:
        print(-1, end=" ")
    index = 0
