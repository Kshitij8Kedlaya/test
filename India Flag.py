import pygame 
pygame.init()
screen = pygame.display.set_mode([1000,600])
pygame.display.set_caption("India Flag")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,(244, 196, 48),(0,0,1000,200))
    pygame.draw.rect(screen,(255,255,255),(0,200,1000,200))
    pygame.draw.rect(screen,(19, 136, 8),(0,400,1000,400))
    pygame.draw.circle(screen,(0, 0, 128),(500,300),90)

    
    pygame.display.update()

pygame.quit()