def factorial(n):
  ans = 1
  for j in range(1, n + 1):
    ans = ans * j % (2**32)
  return ans
n = int(input())
for i in range(n):
  num = int(input())
  if num > 50:
    print(0)
  else:
    print(factorial(num))