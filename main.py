#!/bin/env python3
walls = {0:" ", 1:"│", 2:"─", 3:"┘", 4:"┐", 5:"┌", 6:"└", 7:"┴", 8:"┤", 9:"┬", 10:"├", 11:"┼"}

def new_map(h, w):
    map = [[(0, 1) for rj in range(w)] for j in range(h)]
    return map

def generate(map):
    for j in range (len(map[0])):
        map[0][j] = (2, 1)
        map[len(map)-1][j] = (2, 1)
    for j in range (len(map)):
        map[j][0] = (1, 1)
        map[j][len(map[0])-1] = (1, 1)
    map[0][0] = (5, 1)
    map[len(map)-1][0] = (6, 1)
    map[0][len(map[0])-1] = (4, 1)
    map[len(map)-1][len(map[0])-1] = (3, 1)
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
