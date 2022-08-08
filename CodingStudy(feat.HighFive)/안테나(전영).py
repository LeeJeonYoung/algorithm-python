n = int(input())
x=[]
z=[]
x.append(input().split(' '))
y = list(map(int, x[0]))
avr = sum(y)//n
for i in set(y):
    z.append(abs(i-avr))
a = min(z)
print(avr-a)