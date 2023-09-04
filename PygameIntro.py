import pygame 
pygame.init()
screen = pygame.display.set_mode([500,500])
pygame.display.set_caption("First Pygame")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((50,100,180))
    pygame.draw.circle(screen,(100,60,150),(300,300),100)
    pygame.draw.rect(screen,(127,255,212),(10,10,100,200))
    pygame.draw.line(screen,(0,0,255),(60,30),(90,60),5)
    pygame.draw.line(screen,(0,255,0),(90,60),(120,30),5)
 

    
    pygame.display.update()

pygame.quit()