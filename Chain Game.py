import pygame
import time
import random
pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont('baskervilleoldface',40)
MAGENTA = (220,20,60)
PURPLE = (138,43,226)
CYAN = (0,255,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
snake_size = 10
running = True
def message(msg,color):
    mesg = font.render(msg,True,color)
    screen.blit(mesg,[200,50])
def msgg(msg,color):
    masg = font.render(msg,True,color)
    screen.blit(masg,[width/2,height/2])

def game_loop():
    x = 0
    y = 0
    change_x = 200
    change_y = 200
    game_over = False
    game_close = False
    foodx = round(random.randrange(0,width-snake_size / 10.0)*10.0)
    foody = round(random.randrange(0,height-snake_size/10.0)*10.0)

    while not game_over:
        while game_close == True:
            screen.fill(MAGENTA)
            msgg("You LOST :( \n Press Q to quit OR SPACE key to Play Again",PURPLE)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True
                        if event.key == pygame.K_SPACE:
                            game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x += 10
                    y = 0
                if event.key == pygame.K_DOWN:
                    y += 10
                    x = 0
                if event.key == pygame.K_LEFT:
                    x -= 10
                    y = 0
                if event.key == pygame.K_UP:
                    y -= 10
                    x = 0
        change_x = change_x + x
        change_y = change_y + y
        if change_x > width or change_x < 0 or change_y > height or change_y < 0:
            game_close = True
        message("Your Score:",BLACK)
        pygame.draw.rect(screen,MAGENTA,(change_x,change_y,25,25))
        pygame.draw.rect(screen,PURPLE,(foodx,foody,snake_size,snake_size))
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

game_loop()