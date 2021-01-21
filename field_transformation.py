from settings import *

maps = [
    [
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
    ],
    [
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
    ],
    [
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '......WWWWWWWWWWWW......',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
    ],
    [
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
        '........................',
    ]
]

world_map1 = set()
world_map2 = set()
world_map3 = set()
world_map4 = set()

for j, row in enumerate(maps[0]):
    for i, char in enumerate(row):
        if char in 'W':
            world_map1.add((i * TILE, j * TILE))

for j, row in enumerate(maps[1]):
    for i, char in enumerate(row):
        if char in 'W':
            world_map2.add((i * TILE, j * TILE))

for j, row in enumerate(maps[2]):
    for i, char in enumerate(row):
        if char in 'W':
            world_map3.add((i * TILE, j * TILE))

for j, row in enumerate(maps[3]):
    for i, char in enumerate(row):
        if char in 'W':
            world_map4.add((i * TILE, j * TILE))


'''[
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
        '........................................',
    ],'''