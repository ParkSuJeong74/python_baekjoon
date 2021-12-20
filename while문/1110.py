import sys

n = int(sys.stdin.readline())  # 26
index = 1
tmp = n

while True:
    a = tmp // 10  # 2
    b = tmp % 10  # 6
    c = (a+b) % 10  # 8
    result = (10 * b) + c  # 68

    if result == n:
        break
    tmp = result
    index += 1
print(index)
