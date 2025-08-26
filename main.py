import pygame
import random
import math

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode( (WIDTH, HEIGHT) )

pygame.display.set_caption("2 Planet Gravity Sim")
icon = pygame.image.load("planet.png")
pygame.display.set_icon(icon)

planet_img = []
planetX = []
planetY = []
#planetX_change = []
#planetY_change = []
planet_mass = []
num_of_planets = 2
planetVX = []
planetVY = []

G = 6.67 * (10 ** -11)

for i in range(num_of_planets):
    planet_img.append(pygame.image.load("planet.png"))
    planetX.append(random.randint(0, 736))
    planetY.append(random.randint(0, 536))
    planet_mass.append(10**14)
    planetVX.append(0.0)
    planetVY.append(0.0)

camX, camY = 0, 0
zoom = 1.0
def planet(x, y, i):
    screen_x = (x - camX) * zoom + WIDTH // 2
    screen_y = (y - camY) * zoom + HEIGHT // 2
    img = pygame.transform.scale(planet_img[i], (int(32 * zoom), int(32 * zoom)))
    screen.blit(img, (screen_x, screen_y))

clock = pygame.time.Clock()

# Game Loop
running = True
while running:
    dt = (clock.tick(60) / 1000.0)*10 # 1 SECOND * 10
    screen.fill((255, 255, 255))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEWHEEL:
            if event.y > 0:
                zoom *= 1.1
            elif event.y < 0:
                zoom /= 1.1

    dx = planetX[1] - planetX[0]
    dy = planetY[1] - planetY[0]

    r = math.sqrt(dx ** 2 + dy ** 2)
    if r != 0:
            F = G * planet_mass[0] * planet_mass[1] / r**2

            # force components
            Fx = F * dx / r
            Fy = F * dy / r

            # acceleraion
            ax0 = Fx / planet_mass[0]
            ay0 = Fy / planet_mass[0]
            ax1 = -Fx / planet_mass[1]
            ay1 = -Fy / planet_mass[1]

            # velocity
            planetVX[0] += ax0 * dt
            planetVY[0] += ay0 * dt
            planetVX[1] += ax1 * dt
            planetVY[1] += ay1 * dt

    # Position update
    for i in range(num_of_planets):
        planetX[i] += planetVX[i] * dt
        planetY[i] += planetVY[i] * dt
        planet(planetX[i], planetY[i], i)


    pygame.display.update()