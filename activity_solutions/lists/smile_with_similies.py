a = int(input())
c = []
b = int(input())
d = []

for i in range(a):
  c.append(input())

for i in range(b):
  d.append(input())

for i in range(a):
  for j in range(b):
    print(c[i] + " as " + d[j])