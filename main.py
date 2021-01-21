import pygame
# from settings import *
# import math
from field_transformation import *

pygame.init()
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

GAME_OVER = False

i = 0
a = b = 0
angle = 90

score = 0
record = 0

start = True
flag = False
flag_move = True

coaf_angle = 0

font_end = pygame.font.SysFont('Arial', 66, bold=True)
font_score = pygame.font.SysFont('Arial', 26, bold=True)
render_end1 = font_end.render('Press SPACE to start', 1, pygame.Color(BLUE))
texture = pygame.image.load('img/fon.jpg').convert()


def route_arr(arr1):
    arr2 = []
    s = ''
    for i in range(len(arr1[0])):
        for j in range(len(arr1)):
            s += arr1[j][i]
        arr2.append(s)
        s = ''
    return arr2


def get_record(): # ЗАПИСАТЬ РЕКОРД
    try:
        with open('record_S') as f:
            return f.readline()
    except FileNotFoundError:
        with open('record_S', 'w') as f:
            f.write('0')


def set_record(record, score): # ПОЛУЧИТЬ РЕКОРД
    rec = max(int(record), score)
    with open('record_S', 'w') as f:
        f.write(str(rec))


def clear_code(): # ДЛЯ ЧИСТОТЫ КОДА
    ray_casting(sc, (int(a), int(b)), player_angle, world_map1, 4)
    ray_casting(sc, (int(a), int(b)), player_angle, world_map2, 5)
    ray_casting(sc, (int(a), int(b)), player_angle, world_map3, 6)
    ray_casting(sc, (int(a), int(b)), player_angle, world_map4, 7)
    world_map1.clear()
    for j, row in enumerate(maps[0]):
        for i, char in enumerate(row):
            if char in 'W':
                world_map1.add((i * TILE, j * TILE))
    world_map2.clear()
    for j, row in enumerate(maps[1]):
        for i, char in enumerate(row):
            if char in 'W':
                world_map2.add((i * TILE, j * TILE))
    world_map3.clear()
    for j, row in enumerate(maps[2]):
        for i, char in enumerate(row):
            if char in 'W':
                world_map3.add((i * TILE, j * TILE))
    world_map4.clear()
    for j, row in enumerate(maps[3]):
        for i, char in enumerate(row):
            if char in 'W':
                world_map4.add((i * TILE, j * TILE))


def ray_casting(sc, player_pos, player_angle, lst, h):
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    for ray in range(NUM_RAYS):
        sin_a = -math.sin(cur_angle)
        cos_a = -math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a

            if (x // TILE * TILE, y // TILE * TILE) in lst:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = 50  # min(PROJ_COEFF / (depth + 0.0001), HEIGHT)
                c = 255 / (1 + depth * depth * 0.000005)
                color = (c, c, c)
                pygame.draw.rect(sc, color, (ray * SCALE, HEIGHT - proj_height * h, SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE


'''def mapping(a, b):
    return (a // TILE) * TILE, (b // TILE) * TILE

yv, xh = 0, 0

def ray_casting(sc, player_pos, player_angle, lst, h, texture):
    global yv, xh
    cur_angle = player_angle - HALF_FOV
    xo, yo = player_pos
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    for ray in range(NUM_RAYS):
        sin_a = -math.sin(cur_angle)
        cos_a = -math.cos(cur_angle)
        sin_a = sin_a if sin_a else 0.000001
        cos_a = cos_a if cos_a else 0.000001

        # verticals
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, WIDTH, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in lst:
                break
            x += dx * TILE

        # horizontals
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, HEIGHT, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in lst:
                break
            y += dy * TILE
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a

            if (x // TILE * TILE, y // TILE * TILE) in lst:
                depth, offset = (depth_v, yv) if depth_v < depth_h else (depth_h, xh)
                # depth *= math.cos(player_angle - cur_angle)
                depth *= math.cos(player_angle - cur_angle)
                depth = max(depth, 0.00001)
                proj_height = 50 # min(int(PROJ_COEFF / depth), 8 * HEIGHT)
                offset = int(offset) % TILE
                c = 255 / (1 + depth * depth * 0.000005)
                color = (c // 2, c, c)
                pygame.draw.rect(sc, color, (ray * SCALE, HEIGHT - proj_height * h, SCALE, proj_height))

                wall_column = texture.subsurface(offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT)
                wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
                sc.blit(wall_column, (ray * SCALE, HEIGHT - proj_height * h))
                print(depth)
                break
        cur_angle += DELTA_ANGLE'''


class Cake: # СОЗДАНИЕ СЛОЁВ
    def __init__(self, flag, field):
        global MAX, MIN
        self.flag = flag
        self.field = field

        if self.flag:
            length = 0
            for j in range(HEIGHT * 4 // 100):
                if 'W' in self.field[j]:
                    self.field[j] = self.field[j].replace('.', '')
                    length = len(self.field[j])
            length = len(self.field[0]) - length
            for j in range(HEIGHT * 4 // 100):
                if 'W' in self.field[j]:
                    self.field[j] += '.' * length
                # print(self.field[j], end='\n')
        else:
            while 'W' not in self.field[0]:
                del self.field[0]
                self.field.append(len(self.field[0]) * '.')
            # print(*self.field, sep='\n')
        self.arr = route_arr(self.field)

    def game(self):
        global flag_move
        if self.flag:
            if flag_move:
                self.arr.insert(0, '........................')
                del self.arr[-1]
                maps[3] = route_arr(self.arr)
                if 'W' in self.arr[-2]:
                    flag_move = not flag_move
            else:
                self.arr.append('........................')
                del self.arr[0]
                maps[3] = route_arr(self.arr)
                if 'W' in self.arr[1]:
                    flag_move = not flag_move

        else:
            if flag_move:
                self.field.insert(0, '........................')
                del self.field[-1]
                maps[3] = self.field
                if 'W' in self.field[-2]:
                    flag_move = not flag_move
            else:
                self.field.append('........................')
                del self.field[0]
                maps[3] = self.field
                if 'W' in self.field[1]:
                    flag_move = not flag_move

    def draw(self):
        global score, GAME_OVER, sc
        arr = []
        s = ''
        x = 0
        for i in range(len(maps[0])):
            for j in range(len(maps[0][0])):
                if maps[2][i][j] == 'W' and maps[3][i][j] == 'W':
                    s += 'W'
                    x += 1
                else:
                    s += '.'
            arr.append(s)
            s = ''
        if x == 0:
            GAME_OVER = True
        else:
            score += 1
        maps[3] = arr
        for i in range(len(maps) - 1):
            maps[i] = maps[i + 1]


cake1 = Cake(flag, maps[2].copy())

while True: # ОСНОВНОЙ ИГРОВОЙ ЦИКЛ
    sc.fill(BLACK)
    sc.blit(texture, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                start = False
                flag = not flag
                player_angle = 6
                clear_code()
                while coaf_angle <= angle:
                    sc.fill(BLACK)
                    sc.blit(texture, (0, 0))
                    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('black'))
                    sc.blit(render_score, (20, 5))
                    render_score1 = font_score.render(f'RECORD: {record}', 1, pygame.Color('black'))
                    sc.blit(render_score1, (450, 5))
                    player_angle = coaf_angle * 3.14 / 180
                    a = 600 * math.cos(player_angle) + HALF_WIDTH
                    b = 600 * math.sin(player_angle) + HALF_HEIGHT
                    clear_code()
                    coaf_angle += 3
                    pygame.display.flip()
                if angle == 360:
                    angle = 90
                else:
                    angle += 90
                if coaf_angle >= 360:
                    coaf_angle = 0
                cake1.draw()
                if not GAME_OVER:
                    cake1 = Cake(flag, maps[2].copy())

    record = get_record()
    if start:
        if i <= 360:
            player_angle = i * 3.14 / 180
            sc.fill(BLACK)
            sc.blit(texture, (0, 0))
            sc.blit(render_end1, (WIDTH // 2 - 275, HEIGHT // 4))
            a = 600 * math.cos(player_angle) + HALF_WIDTH
            b = 600 * math.sin(player_angle) + HALF_HEIGHT
            i += 3
        else:
            i = 0
        clear_code()

    cake1.game()
    clear_code()

    if GAME_OVER:
        sc.fill((180, 0, 0))
        over = font_end.render('GAME OVER', 1, pygame.Color('red'))
        sc.blit(over, (20, HALF_HEIGHT))
        set_record(record, score)

    render_score = font_score.render(f'SCORE: {score}', 1, pygame.Color('black'))
    sc.blit(render_score, (20, 5))
    render_score1 = font_score.render(f'RECORD: {record}', 1, pygame.Color('black'))
    sc.blit(render_score1, (450, 5))

    pygame.display.flip()
    clock.tick()
