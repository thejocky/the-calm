import pytest
from main import tile, dungeon

def test_dungeon_find_wall():
    layout = [[tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL],
        [tile.WALL, tile.NUL, tile.NUL, tile.NUL, tile.NUL, tile.WALL, tile.NUL, tile.NUL, tile.NUL, tile.WALL],
        [tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL],
        [tile.WALL, tile.NUL, tile.NUL, tile.NUL, tile.NUL, tile.WALL, tile.NUL, tile.NUL, tile.NUL, tile.WALL],
        [tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL, tile.WALL]]

    expect = """┌────┬───┐
│    │   │
├────┼───┤
│    │   │
└────┴───┘"""

    d = dungeon(10, 5)
    d.layout = layout
    assert d.print() == expect
