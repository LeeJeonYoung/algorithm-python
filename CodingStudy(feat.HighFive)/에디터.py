from collections import deque
str = deque(input())
num = int(input())
length = len(str)
idx = length

for _ in range(num):
    x=input().split(" ")

    if x[0] == "P":
        if 0 <=idx<=length:
            str.insert(idx, x[1])
            idx+=1

    elif x[0] == "L":
        if idx != 0:
            idx = idx -1

    elif x[0] == "D":
        if idx != length:
            idx = idx + 1

    elif x[0] == "B":
        if idx != 0:
            del str[idx-1]
            idx -= 1
answer = "".join(str)
print(answer)