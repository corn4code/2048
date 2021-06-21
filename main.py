import pygame


pygame.init()
window_width = 600
window_height = 600
size = [window_width, window_height]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
background_grey = [205, 193, 180]
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(background_grey)

    clock.tick(144)
pygame.quit()
