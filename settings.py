import math

# game settings
WIDTH = 600
HEIGHT = 600
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 30
TILE = 25

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 100
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS

# texture settings (1200 x 1200)
TEXTURE_WIDTH = 300
TEXTURE_HEIGHT = 300
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# player settings
player_pos = (HALF_WIDTH - 500, HALF_HEIGHT)
player_angle = 6 # 1.57 + 1.57
player_speed = 5

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (220, 0, 0)
GREEN = (0, 250, 0)
BLUE = (23, 89, 127)
DARKGRAY = (40, 40, 40)
PURPLE = (101, 36, 202)

# platforms
MIN = 0
MAX = 10


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