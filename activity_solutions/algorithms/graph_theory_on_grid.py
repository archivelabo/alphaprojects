g = [[0 for y in range(8)] for x in range (8)]

sc, sr = map(int, input().split())
ec, er = map(int, input().split())
sc -= 1
sr -= 1
ec -= 1
er -= 1

dc = [2, 2, -2, -2, -1, -1, 1, 1]
dr = [1, -1, 1, -1, 2, -2, 2, -2]
g[sr][sc] = 1
q = [] # grid
q.append([sr, sc])
q.append(None)
d = 1 # distance
end = False
while q:
    if end:
        break
    t = q.pop(0)
    if t == None:
        if not q or q[0] == None:
            break
        d += 1
        q.append(None)
        continue
    for i in range(8):
        r2 = t[0] + dr[i]
        c2 = t[1] + dc[i]
        try:
            g[r2][c2]
        except:
            continue
        if r2 == er and c2 == ec:
            end = True
            break
        if not g[r2][c2] and r2 > -1 and c2 > -1:
            g[r2][c2] = 1
            q.append([r2, c2])


if sc == ec and sr == er:
    d = 0
print(d)
