#!/bin/env python3
walls = {0:" ", 1:"│", 2:"─"}

def new_map(h, w):
    map = [[(1, 1) for rj in range(w)] for j in range(h)]
    return map

def generate(map):
    for j in range (len(map[0])):
        map[0][j] = (2, 1)
    return map

def print_dungeon(dungeon):
    for j in dungeon:
        for k in j:
            if k[1]:
                print (walls[k[0]], end="")
            else:
                print (" ", end="")
        print()
    print()


m = new_map(5, 10)
m = generate(m)
for j in m:
    print (j)
    print ()
print_dungeon(m)
