정답

from collections import defaultdict
from itertools import combinations

def solution(places):
    answer = []
    dict = defaultdict(list)
    dict2 = defaultdict(list)
    
    # print(places)
    for i in range(5):
        # print(places[i])
        for j in range(5):
            for k in range(5):
                if places[i][j][k] =='P':
                    dict[str(i+1)+'대기실'].append([j,k])
                elif places[i][j][k] =='X':
                    dict2[str(i+1)+'대기실 파티션'].append([j,k])
    # print(dict)
    for i in range(5):
        # print(dict[str(i+1)+'대기실'])
        # print(answer)
        if len(dict[str(i+1)+'대기실']) !=0:
            for j in list(combinations(dict[str(i+1)+'대기실'],2)):
                # print(j)
                # print(j[1])
                if abs(j[0][0] - j[1][0]) + abs(j[0][1]-j[1][1]) ==2:
                    if abs(j[0][0] - j[1][0]) ==1:
                        # print(j)
                        # print(dict)
                        X=[j[0][0],j[1][1]]
                        Y=[j[1][0],j[0][1]]
                        if (X not in dict2[str(i+1)+'대기실 파티션'] or  Y not in dict2[str(i+1)+'대기실 파티션']):
                            answer.append(0)
                            break
                    else:
                        X=[(j[0][0] + j[1][0])//2, (j[0][1]+j[1][1])//2]
                        # print(j)
                        # print(X)
                        # print(dict2[str(i+1)+'대기실 파티션'])
                        if X not in dict2[str(i+1)+'대기실 파티션']:
                            answer.append(0)
                            break
                elif abs(j[0][0] - j[1][0]) + abs(j[0][1]-j[1][1]) ==1:
                    answer.append(0)
                    break
            # print(answer)
        if len(answer) ==0 or len(answer) <=i:
            answer.append(1)
        # print(dict2[str(i+1)+'대기실 파티션'])
    # print(dict)
    # print(dict2)
    return answer
