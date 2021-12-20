number = list(map(int, input().split()))

sum = 0
for i in number:
    sum += i * i
chk = sum % 10

print(chk)
