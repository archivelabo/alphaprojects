n = int(input())

people = []
for i in range(n):
    people.append(input().split())

people_sorted = sorted(people, key=lambda x: int(x[1]))

for person in people:
    if people_sorted.index(person) > n / 2:
        print(person[0] + " is cute! <3 ")
    else:
        print(person[0] + " is not cute! </3 ")