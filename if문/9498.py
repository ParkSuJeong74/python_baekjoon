score = input()

if int(score) <= 100 and int(score) >= 90:
    print('A')
elif int(score) < 90 and int(score) >= 80:
    print('B')
elif int(score) < 80 and int(score) >= 70:
    print('C')
elif int(score) < 70 and int(score) >= 60:
    print('D')
else:
    print('F')
