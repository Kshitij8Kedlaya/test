import pygame
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("AWSD keys")
MAGENTA = (220,20,60)
PURPLE = (138,43,226)
CYAN = (0,255,255)
flag = True
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("You have pressed 'a' key")
            if event.key == pygame.K_w:
                print("You have pressed 'w' key")
            if event.key == pygame.K_s:
                print("You have pressed 's' key")
            if event.key == pygame.K_d:
                print("You have pressed 'd' key")

            if event.key == pygame.K_c:
                pygame.draw.circle(screen,CYAN,(300,300),100)
            if event.key == pygame.K_r:
                pygame.draw.rect(screen,MAGENTA,(10,10,100,200))
            if event.key == pygame.K_l:
                pygame.draw.line(screen,PURPLE,(150,100),(300,150),10)
            
            pygame.draw.line(screen,PURPLE,[width/2,height/2],[width-20,height-30],4)

    pygame.display.update()

pygame.quit()