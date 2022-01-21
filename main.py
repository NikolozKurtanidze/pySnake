from random import randrange
from tokenize import Whitespace
from typing import List, Tuple
import pygame, os

RUN = True
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE  = (0, 0, 255)
RED = (255, 0, 0)
FPS = 8
SCORE = 0
pygame.init()
WIDTH, HEIGHT = 400, 400
WIN = pygame.display.set_mode((800, 800))
pygame.display.set_icon(pygame.image.load(os.path.join('Icon', 'icon.png')))
pygame.display.set_caption('pySnake')

def draw(snake_body, food_x, food_y, board = None):
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render(str(SCORE), True, BLACK)
    WIN.fill(WHITE)
    WIN.blit(text, (200, 168))
    pygame.draw.rect(WIN, BLACK, pygame.Rect(200, 200, 400, 400))
    pygame.draw.rect(WIN, RED, pygame.Rect(food_x, food_y, 20, 20))
    pygame.draw.rect(WIN, BLUE, pygame.Rect(snake_body[0][0], snake_body[0][1], 20, 20))
    for i in snake_body:
        pygame.draw.rect(WIN, BLUE, pygame.Rect(i[0], i[1], 20, 20))
    pygame.display.update()

def body_move(snake_body):
    global RUN
    for i in range(len(snake_body) - 1, 0, -1):
        snake_body[i] = snake_body[i - 1]

def main():
    global SCORE
    global RUN
    clock = pygame.time.Clock()
    snake_body = []
    snake_body.append(((randrange(0, 20) * 20) + 200, (randrange(0, 20) * 20) + 200))
    food_x, food_y = 260, 260
    move = 'n'
    key = pygame.key.get_pressed()
    while RUN:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and move != 'l':
                    move = 'r'
                elif event.key == pygame.K_w and move != 'd':
                    move = 'u'
                elif event.key == pygame.K_a and move != 'r':
                    move = 'l'
                if event.key == pygame.K_s and move != 'u':
                    move = 'd'
        if snake_body[0][0] == food_x and snake_body[0][1] == food_y:
            SCORE += 1
            food_x = randrange(200, WIDTH + 200, 20)
            food_y = randrange(200, HEIGHT + 200, 20)
            snake_body.append(snake_body[-1])
        if move == 'r' and snake_body[0][0] >= WIDTH + 180:
            main()
            break
        if move == 'l' and snake_body[0][0] <= 200:
            main()
            break
        if move == 'u' and snake_body[0][1] <= 200:
            main()
            break
        if move == 'd' and snake_body[0][1] >= HEIGHT + 180:
            main()
            break
        if move == 'r':
            snake_body[0] = (snake_body[0][0] + 20, snake_body[0][1])
        elif move == 'l':
            snake_body[0] = (snake_body[0][0] - 20, snake_body[0][1])
        elif move == 'u':
            snake_body[0] = (snake_body[0][0], snake_body[0][1] - 20)
        elif move == 'd':
            snake_body[0] = (snake_body[0][0], snake_body[0][1] + 20)
        draw(snake_body, food_x, food_y)
        if snake_body[0] in snake_body[1:len(snake_body)]:
            main()
        body_move(snake_body)
        




if __name__ == '__main__':
    main()
