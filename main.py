#!/bin/env python3
walls = {0:" ", 3:"│", 7:"│", 10:"│", 5:"─", 11:"─", 16:"─", 14:"┘", 18:"┐", 12:"┌", 8:"└", 19:"┴", 21:"┤", 23:"┬", 15:"├", 26:"┼"}

def new_map(h, w):
    map = [[(0, 1) for rj in range(w)] for j in range(h)]
    return map

def generate(map):
    for j in range (len(map[0])):
        map[0][j] = (1, 1)
        map[len(map)-1][j] = (1, 1)
        map[(len(map))//2][j] = (1, 1)
    for j in range (len(map)):
        map[j][0] = (1, 1)
        map[j][len(map[0])-1] = (1, 1)
        map[j][(len(map[0]))//2] = (1, 1)
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



# above = 3, right = 5, bottom = 7, left = 11
def find_wall_type(dungeon):
    for j in range(len(dungeon)):
        for k in range(len(dungeon[0])):
            value = 0
            if dungeon[j][k][0]:
                if j:
                    if dungeon[j-1][k][0]:
                        value += 3
                if k:
                    if dungeon[j][k-1][0]:
                        value += 11
                if j != len(dungeon)-1:
                    if dungeon[j+1][k][0]:
                        value += 7
                if k != len(dungeon[0])-1:
                    if dungeon[j][k+1][0]:
                        value += 5
            dungeon[j][k] = (value, dungeon[j][k][1])
    return dungeon




m = new_map(10, 20)
m = generate(m)
for j in m:
    print (j)
    print ()
m = find_wall_type(m)
for j in m:
    print (j)
    print ()
print_dungeon(m)
