def new_map(h, w):
    map = [[False for rj in range(w)] for j in range(h)]
    return map

def generate(map):
    for j in range (len(map[0])):
        map[0][j] = True
    return map


m = new_map(5, 10)
m = generate(m)
for j in m:
    print (j)
    print ()
