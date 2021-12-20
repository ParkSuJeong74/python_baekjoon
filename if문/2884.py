h, m = input().split()
hour = int(h)
min = int(m)

if min >= 45:
    print(hour, min-45)
elif hour >= 1 and min < 45:
    print(hour-1, min+60-45)
else:
    print(hour+23, min+60-45)
