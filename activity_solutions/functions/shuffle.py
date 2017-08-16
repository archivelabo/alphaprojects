from fractions import gcd

def cycCount(t, cur, i):
  if two[code(cur)]:
    return i
  two[code(cur)] = True
  one[code(cur)] = cycCount(t, t[code(cur)], i + 1)
  return one[code(cur)]

def char(x):
  if x == 26:
    x = 30
  return(chr(x + 65))

def code(x):
  x = ord(x) - 65
  if x == 30:
    x = 26
  return x

one = [0] * 27
two = [0] * 27
three = [0] * 27

for i in range(27):
  three[i] = input()
for i in range(27):
  cycCount(three, char(i), 0)

n = int(input())
s = list(input())
l = one[0]

for i in range(1, 27):
  l = l * one[i] / gcd(l, one[i])
n %= l

for i in range(int(n)):
  temp = s
  for j in range(len(s)):
    temp[j] = three[code(temp[j])]
  s = temp

for l in s:
  print(l, end="")
