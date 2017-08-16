n = int(input())
h = 0
for i in range(n):
    x = int(input())
    if x > h: h = x

if h > 10000:
    print("Something is wrong with these cuteness values")
elif h > 1000:
    print("Cuteness by definition is similarity to Cactus")
else:
    print("Cuteness by definition is similarity to Carol")