N = input()
x = len(N)//2
sum1 =0
sum2 = 0
for i in range(x):
    sum1 += int(N[i])
for x in range(x):
    sum2 += int(N[-(x+1)])
if sum1 == sum2:
    print("LUCKY")
else:
    print("READY")