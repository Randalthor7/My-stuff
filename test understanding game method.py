import pygame, sys,random
from pygame.math import Vector2


class SNAKE:
    def __init__(self):
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
    def move_snake(self):
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy       
for i in range(0,5):
    snake = SNAKE()
    print(snake.body)
    snake.move_snake()
    print(snake.body)

