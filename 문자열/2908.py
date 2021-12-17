import sys

number = list(sys.stdin.readline().split())
string1 = str(int(number[0]) % 10) + \
    str(int(number[0])//10 % 10) + str(int(number[0])//100)
string2 = str(int(number[1]) % 10) + \
    str(int(number[1])//10 % 10) + str(int(number[1])//100)

if int(string1) > int(string2):
    print(string1)
else:
    print(string2)
