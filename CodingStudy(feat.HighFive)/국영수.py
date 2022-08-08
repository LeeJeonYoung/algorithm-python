import sys
n = input()

x = []

for i in range(int(n)):
    x.append(sys.stdin.readline().strip().split(' '))
b = sorted(x,key = lambda x: (-int(x[1]),int(x[2]),-int(x[3]),x[0]))
for i in range(len(b)):
    print(b[i][0])