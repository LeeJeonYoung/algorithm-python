n = int(input())
x = []
x = list(map(int, input().rstrip().split()))
x.sort()
print(x[(n-1)//2])
