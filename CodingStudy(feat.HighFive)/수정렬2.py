import sys
n = int(input())
x = []
for i in range(n):
    x.append(int(sys.stdin.readline()))

for i in sorted(x):
    sys.stdout.write(str(i)+'\n')