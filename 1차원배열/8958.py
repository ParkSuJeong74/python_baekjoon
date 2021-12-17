import sys

n=int(sys.stdin.readline())

for j in range(n):
    ox = list(str(sys.stdin.readline()))
    score = 0
    index = 0
    for i in range(len(ox)):
        if ox[i] == 'O':
            score += 1+ index
            index += 1
        elif ox[i] == 'X' :
            index = 0
    print(score, end="\n")