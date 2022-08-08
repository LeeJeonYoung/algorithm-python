import math

def is_prime_number(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True
import sys
a,b = map(int,sys.stdin.readline().strip().split(' '))
for i in range(a,b+1):
  if is_prime_number(i):
    print(i)