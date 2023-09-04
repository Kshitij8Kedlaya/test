import pygame
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("AWSD keys")
MAGENTA = (220,20,60)
PURPLE = (138,43,226)
CYAN = (0,255,255)
x = 10
y = 10
flag = True
while flag:
    screen.fill(CYAN)
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                x += 50
            if event.key == pygame.K_s:
                y += 50
            if event.key == pygame.K_a:
                x -= 50
            if event.key == pygame.K_UP:
                y -= 50
            
    pygame.draw.rect(screen,MAGENTA,(x,y,40,40))

    pygame.display.update()

pygame.quit()