import pygame
import pygame.draw


pygame.init()

width = 1000
height = 1000
screen = pygame.display.set_mode((width,height))
middle_x = width  /2
middle_y = height  /2
grid_width=10
grid_height=10

COLOR = (55, 200, 80)
screen.fill(COLOR)
snake = [(0, middle_y+1),(0, middle_y+1) ]



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    # pygame.draw.circle(screen, (70, 20, 240), (middle_x,middle_y), 100)



pygame.quit()
