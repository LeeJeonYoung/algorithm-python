a,b = map(int, input().split(" "))
# 18 4
c = a // b
c2 = c
c3 = c
# c= 4
answer=[]

# answer=[4]
while True:
    c = a // b
    answer.append(c)

    if sum(answer) == a and c == 1 and len(answer) >= a//2:
        break
    elif sum(answer) + c2+1 <= a:
        c2+=1
        answer.append(c2)
    elif sum(answer) + c3 -1 <= a and c3 >0:
        c3 -= 1
        answer.append(c3)

    if len(answer) == b and sum(answer) !=a:
        b +=1
        c2=c
        c3=c
        answer=[]
    print(answer)










