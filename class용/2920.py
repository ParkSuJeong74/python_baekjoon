import sys

music = input()

if music == "1 2 3 4 5 6 7 8":
    # ascending
    print("ascending")
elif music == "8 7 6 5 4 3 2 1":
    # d
    print("descending")
else:
    print("mixed")