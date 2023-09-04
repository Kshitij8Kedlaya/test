import pygame
pygame.init()
screen = pygame.display.set_mode([900,600])
pygame.display.set_caption("Italy Flag")

flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
    pygame.draw.rect(screen,(0,140,69),(0,0,300,600))
    pygame.draw.rect(screen,(244, 249, 255),(300,0,600,600))
    pygame.draw.rect(screen,(205, 33, 42),(600,0,900,600))

    pygame.display.update()

pygame.quit()

