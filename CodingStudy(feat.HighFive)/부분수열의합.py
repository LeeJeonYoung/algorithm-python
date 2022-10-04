from itertools import combinations
N,S = map(int, input().split(" "))
array = input().split(" ")
answer=[]
cnt=0
for i in range(len(array)):
    array[i] = int(array[i])

for i in range(1,N+1):
    answer.extend(list(combinations(array,i)))

for i in answer:
    if sum(i) == S:
        cnt +=1

print(cnt)