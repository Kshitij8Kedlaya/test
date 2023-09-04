import pygame
import random
import time

pygame.init()
width = 600
height = 600
screen = pygame.display.set_mode([width,height])
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont('baskervilleoldface',20)
MAGENTA = (220,20,60)
PURPLE = (138,43,226)
CYAN = (0,255,255)
BLACK = (0,0,0)
WHITE = (255,255,255)
snake_size = 25
snake_list = []

running = True
def message(msg,color):
    mesg = font.render(msg,True,color)
    screen.blit(mesg,[200,50])
def msgg(msg,color):
    masg = font.render(msg,True,color)
    screen.blit(masg,[width/2,height/2])
def replay(msg,color):
    misg =  font.render(msg,True,color)
    screen.blit(misg,[10,10])
def our_snake(snake_size,snake_list):
    for i in snake_list:
        pygame.draw.rect(screen,MAGENTA,(i[0],i[1],snake_size,snake_size))

def game_loop():
    x = 0
    y = 0
    change_x = 200
    change_y = 200
    game_over = False
    game_close = False
    foodx = round(random.randrange(0,width-snake_size) / 10.0)*10.0
    foody = round(random.randrange(0,height-snake_size) /10.0)*10.0
    length_of_snake = 1

    while not game_over:
        while game_close == True:
            screen.fill(MAGENTA)
            replay("You LOST :( Press Q to quit OR Space to Play Again",PURPLE)
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
                    x += 5
                    y = 0
                if event.key == pygame.K_DOWN:
                    y += 5
                    x = 0
                if event.key == pygame.K_LEFT:
                    x -= 5
                    y = 0
                if event.key == pygame.K_UP:
                    y -= 5
                    x = 0
        change_x = change_x + x
        change_y = change_y + y
        if change_x > width or change_x < 0 or change_y > height or change_y < 0:
            game_close = True
        screen.fill(CYAN)
        message("Your Score:",BLACK)
        pygame.draw.rect(screen,MAGENTA,(change_x,change_y,snake_size,snake_size))
        pygame.draw.rect(screen,PURPLE,(foodx,foody,snake_size,snake_size))
        snake_head = []
        snake_head.append(change_x)
        snake_head.append(change_y)
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]
        
        for j in snake_list[:-1]:
            if j == snake_head:
                game_close = True
        our_snake(snake_size , snake_list)

        if foodx == change_x and foody == change_y:
            foodx = round(random.randrange(0,width-snake_size) / 10.0)*10.0
            foody = round(random.randrange(0,height-snake_size) /10.0)*10.0
            length_of_snake +=  1
            
        pygame.display.update()
        clock.tick(30)

    pygame.quit()
    quit()

game_loop()