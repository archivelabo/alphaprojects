import math
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True
num = int(input())
f = False
if num == 0:
  print(2)
elif num == 1:
  print(2)
else:
  while not(f):
    f = isPrime(num)
    num += 1

  print(num - 1)
