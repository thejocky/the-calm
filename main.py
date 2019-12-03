#!/bin/env python3
from enum import Enum


class tile(Enum):
    INVALID = 0
    NUL = 1
    WALL = 2
    FLOOR = 3


class dungeon:
    walls = {
        0: " ",
        3: "│",
        7: "│",
        10: "│",
        5: "─",
        11: "─",
        16: "─",
        14: "┘",
        18: "┐",
        12: "┌",
        8: "└",
        19: "┴",
        21: "┤",
        23: "┬",
        15: "├",
        26: "┼",
    }

    def __init__(self, x: int, y: int):
        self.layout = [[tile.NUL for rj in range(x)] for j in range(y)]

    def _tile_is(tile, x: int, y: int):
        return tile == layout[y][x]

    def generate(self):
        for j in range(len(self.layout[0])):
            self.layout[0][j] = tile.WALL
            self.layout[len(self.layout) - 1][j] = tile.WALL
            self.layout[(len(self.layout)) // 2][j] = tile.WALL
        for j in range(len(self.layout)):
            self.layout[j][0] = tile.WALL
            self.layout[j][len(self.layout[0]) - 1] = tile.WALL
            self.layout[j][(len(self.layout[0])) // 2] = tile.WALL

    # above = 3, right = 5, bottom = 7, left = 11
    def find_wall_type(self, x: int, y: int):
        value = 0
        if self.layout[y][x] == tile.WALL:
            if y:
                if self.layout[y - 1][x] == tile.WALL:
                    value += 3
            if x:
                if self.layout[y][x - 1] == tile.WALL:
                    value += 11
            if y != len(self.layout) - 1:
                if self.layout[y + 1][x] == tile.WALL:
                    value += 7
            if x != len(self.layout[0]) - 1:
                if self.layout[y][x + 1] == tile.WALL:
                    value += 5
        return walls[value]

    def print(self):
        out = ""
        for j, v in enumerate(self.layout):
            for i, t in enumerate(v):
                if t == tile.WALL:
                    out += self.find_wall_type(i, j)
                else:
                    out += " "
            if j < len(self.layout) - 1:
                out += "\n"
        return out


m = dungeon(10, 5)
m.generate()

for j in m.layout:
    print(j)
    print()

print(m.print())
