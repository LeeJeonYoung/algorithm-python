
from collections import deque
K, N = map(int,input().split(" "))
n=deque()

for _ in range(K):
    n.append(int(input()))
SumN = sum(n)
mid=0
high = SumN // N +1 #231
low = 0
lowx = 0

def binary2(n, mid):
    cnt=0
    for i in n:
        cnt += i // mid
    return cnt

while True: low 200 high 201
    if mid == (high + low) // 2:
        break
    mid = (high + low) // 2
    cnt=0
    cnt = binary2(n,mid)
    if cnt == N:
        lowx = mid
        mid = (high + lowx) // 2

        if cnt == binary2(n,mid):
            low = mid
        else:
            high = mid
    elif cnt > N:
        low = mid

    elif cnt < N:
        high = mid
print(mid)
