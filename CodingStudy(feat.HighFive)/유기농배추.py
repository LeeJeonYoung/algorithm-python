from collections import defaultdict
nums = int(input())

answer=defaultdict(list)
i=0
for num in range(nums):
    M, N, K = map(int, input().split(" "))
    answer = defaultdict(list)
    print(answer)
    cnt=0
    length=False
    for _ in range(K):
        length=False
        cnt+=1
        a,b = map(int,input().split(" "))

        if len(answer) == 0:
            answer[i].append((a, b))
            print(answer)

        elif len(answer) != 0:
            for j in range(i+1):
                for k in range(len(answer[j])):

                    if sum([a,b]) - sum(answer[j][k]) == 1:
                        answer[j].append((a,b))
                        length = True
                        break

            if length == False:
                i+=1
                answer[i].append((a,b))
            print(answer)
    print(len(answer))