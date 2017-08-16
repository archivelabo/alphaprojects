import sys
input = sys.stdin.readline
n, m = map(int, input().split())
food = [[] for x in range(n + 1)]
for i in range(m):
  recipe = list(map(int, input().split()))
  for x in recipe[2:]:
    food[recipe[0]].append(x)

ingredients = [0] + list(map(int, input().split()))

need = food[1]

def make(f):
  global ingredients
  c = 1
  if food[f]:
    for i in food[f]:
      make(i)
    if c:
      m = 1 << 35
      for i in food[f]:
        try:
          if ingredients[i] < 1:
            return
        except:
          return
        if ingredients[i] < m:
          m = ingredients[i]
      for i in food[f]:
        ingredients[i] -= m
      ingredients[f] += m

make(1)
print(ingredients[1])
