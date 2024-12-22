import math
from collections import defaultdict
import pygame
from dataclasses import dataclass
import re


@dataclass
class Robot:
    x: int
    y: int
    vx: int
    vy: int


def build(fname):
    out = []
    for line in open(fname).readlines():
        p, v = line.split(" ")
        x, y = list(map(int, re.findall(r"\d+", p)))
        vx, vy = list(map(int, re.findall(r"-?\d+", v)))

        out.append(Robot(x, y, vx, vy))

    return out


def has_robot(x, y, robots):
    for r in robots:
        if r.x == x and r.y == y:
            return True
    return False


def safety_factor(robots, h, w):
    mh = h // 2
    mw = w // 2

    out = [0, 0, 0, 0]
    for r in robots:
        if r.x < mh and r.y < mw:
            out[0] += 1
        elif r.x > mh and r.y < mw:
            out[1] += 1
        elif r.x < mh and r.y > mw:
            out[2] += 1
        elif r.x > mh and r.y > mw:
            out[3] += 1

    return math.prod(out)


def track_dispersion(robots):
    if not robots:
        return 0

    xs = [r.x for r in robots]
    ys = [r.y for r in robots]

    mean_x = sum(xs) / len(xs)
    mean_y = sum(ys) / len(ys)

    std_x = (sum((x - mean_x) ** 2 for x in xs) / len(xs)) ** 0.5
    std_y = (sum((y - mean_y) ** 2 for y in ys) / len(ys)) ** 0.5

    # Combine into single value
    combined_std = (std_x**2 + std_y**2) ** 0.5 / 2**0.5
    return combined_std


def calc(robots, h, w, seconds):
    robots = build("input.txt")
    for r in robots:
        new_x = (r.x + r.vx * seconds) % h
        new_y = (r.y + r.vy * seconds) % w
        r.x = new_x
        r.y = new_y

    return robots


def solve1(fname, h, w):
    robots = build(fname)

    k = h * w

    for r in robots:
        assert (r.x + r.vx * k) % h == r.x
        assert (r.y + r.vy * k) % w == r.y

    seconds = 100

    robots = calc(robots, h, w, seconds)

    mh = h // 2
    mw = w // 2
    out = [0, 0, 0, 0]
    for r in robots:
        if r.x < mh and r.y < mw:
            out[0] += 1
        elif r.x > mh and r.y < mw:
            out[1] += 1
        elif r.x < mh and r.y > mw:
            out[2] += 1
        elif r.x > mh and r.y > mw:
            out[3] += 1

    return math.prod(out)


def draw_second(width, height, robots, second):
    # Constants
    CELL_SIZE = 8
    SCREEN_WIDTH = width * CELL_SIZE
    SCREEN_HEIGHT = height * CELL_SIZE
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Robot Second")
    clock = pygame.time.Clock()  # For controlling frame rate
    pygame.font.init()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Draw
        screen.fill(WHITE)

        for r in robots:
            pygame.draw.rect(
                screen,
                BLUE,
                (r.x * CELL_SIZE, r.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

        pygame.display.flip()
        clock.tick(360)  # Limit to 60 FPS

    pygame.quit()


def draw_grid_slideshow(width, height, robots):
    pygame.init()

    # Constants
    CELL_SIZE = 8
    SCREEN_WIDTH = width * CELL_SIZE
    SCREEN_HEIGHT = height * CELL_SIZE

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Robot Grid")
    clock = pygame.time.Clock()  # For controlling frame rate
    pygame.font.init()

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    running = True
    simulating = True
    scenes = [
        35,
        136,
        237,
        338,
        439,
        540,
        641,
        742,
        843,
        944,
        1045,
        1146,
        1247,
        1348,
        1449,
        1550,
        1651,
        1752,
        1853,
        1954,
        2055,
        2156,
        2257,
        2358,
        2459,
        2560,
        2661,
        2762,
        2863,
        2964,
        3065,
        3166,
        3267,
        3368,
        3469,
        3570,
        3671,
        3772,
        3873,
        3974,
        4075,
        4176,
        4277,
        4378,
        4479,
        4580,
        4681,
        4782,
        4883,
        4984,
        5085,
        5186,
        5287,
        5388,
        5489,
        5590,
        5691,
        5792,
        5893,
        5994,
        6095,
        6196,
        6297,
        6398,
        6499,
        6600,
        6701,
        6802,
        6903,
        7004,
        7105,
        7206,
        7307,
        7408,
        7509,
        7610,
        7711,
        7812,
        7913,
        8014,
        8115,
        8216,
        8317,
        8418,
        8519,
        8620,
        8721,
        8822,
        8923,
        9024,
        9125,
        9226,
        9327,
        9428,
        9529,
        9630,
        9731,
        9832,
        9933,
        10034,
        10135,
        10236,
        10337,
    ]
    i = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and i != len(scenes):
                    i += 1
                elif event.key == pygame.K_LEFT and i != 0:
                    i -= 1

        # Draw
        screen.fill(WHITE)
        robots = calc(robots, height, width, scenes[i])

        print(i)

        for r in robots:
            pygame.draw.rect(
                screen,
                BLUE,
                (r.x * CELL_SIZE, r.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

        clock.tick(4)  # Limit to 60 FPS
        pygame.display.flip()

    pygame.quit()


def draw_grid(width, height, robots):
    pygame.init()

    # Constants
    CELL_SIZE = 8
    SCREEN_WIDTH = width * CELL_SIZE
    SCREEN_HEIGHT = height * CELL_SIZE

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Robot Grid")
    clock = pygame.time.Clock()  # For controlling frame rate
    pygame.font.init()
    my_font = pygame.font.SysFont("Comic Sans MS", 30)

    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)

    running = True
    simulating = True
    c = 0
    stds = []
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    simulating = not simulating  # Toggle simulation

        # Draw
        screen.fill(WHITE)
        sf = safety_factor(robots, height, width)
        text_surface = my_font.render(f"sf: {sf} ({c}s)", False, (0, 0, 0))
        stds.append(sf)

        for r in robots:
            if simulating:
                new_x = (r.x + r.vx) % height
                new_y = (r.y + r.vy) % width
                r.x = new_x
                r.y = new_y

            pygame.draw.rect(
                screen,
                BLUE,
                (r.x * CELL_SIZE, r.y * CELL_SIZE, CELL_SIZE, CELL_SIZE),
            )

        if simulating:
            c += 1

        screen.blit(text_surface, (10, 10))
        pygame.display.flip()
        clock.tick(360)  # Limit to 60 FPS
        if c == height * width:
            simulating = False
            with open("stds.txt", "w") as f:
                for s in stds:
                    f.write(f"{s}\n")

    pygame.quit()


# Usage example:
# def get_robot_positions():
#     return your_current_robot_positions
# draw_grid(101, 103, get_robot_positions)


if __name__ == "__main__":
    # t1 = solve1("test.txt", 7, 11)
    # print(t1)
    # assert t1 == 12

    p1 = solve1("input.txt", 101, 103)
    print(p1)
    assert p1 == 219512160

    # draw_second(103, 101, build("input.txt"), 843)
    draw_grid_slideshow(103, 101, build("input.txt"))
