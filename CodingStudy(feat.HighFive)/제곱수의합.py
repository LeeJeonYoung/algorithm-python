import math
n = int(input())
cnt =0
while True:
    if math.sqrt(n/2).is_integer():
        x = math.sqrt(n/2)
    else:
        sqrtN = math.sqrt(n)
        x = math.trunc(sqrtN)
    n = n - pow(x,2)
    cnt += 1
    if n ==0:
        break

print(cnt)