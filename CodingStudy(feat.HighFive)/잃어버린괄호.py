import re
n=input()
n2 = re.split('[-,+]', n)
length = len(n2)
answer=[]
idx=0
x=999999999999

for i in range(len(n)):
    if not n[i].isdigit():
        answer.append(n[idx:i])
        answer.append(n[i])
        idx=i+1
answer.append(n2[-1])
for i in range(2,length+1):
    for j in range(1,length-i+2):
        answer2=answer[:]
        #i는 두점거리 j는 초기값.

        answer2[2*(j-1)] = "(" + answer[2*(j-1)].lstrip("0")
        answer2[2*(j-1)+2*(i-1)] = answer[2*(j-1)+2*(i-1)].lstrip("0")+")"

        if x > eval("".join(answer2)):
            x = eval("".join(answer2))

print(x)

