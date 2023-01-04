import pygame
import random

# Initialize pygame
pygame.init

# Create the screen
screen = pygame.display.set_mode((800,600)) 

# Background
background = pygame.image.load('D:\\My-stuff\\python-game\\images\\background.png')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('D:\\My-stuff\\python-game\\images\\ufo.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('D:\\My-stuff\\python-game\\images\\spaceship.png')
playerX = 370
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('D:\\My-stuff\\python-game\\images\\alien.png')
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 4
enemyY_change = 40


def player(x,y):
    screen.blit(playerImg, (x, y))

def Enemy(x,y):
    screen.blit(enemyImg, (x, y))

#game loop
running = True
while running:
    # RGB values for screen

    screen.fill((0,0,0))

    # Background Image

    screen.blit(background,(0,0) )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed check whether it's right or left.
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
                
            if event.key == pygame.K_RIGHT:
                playerX_change = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # Player movement
    
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    
    # Enemy movement
    
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 4
        enemyY += enemyY_change 
    elif enemyX >= 736:
        enemyX_change = -4
        enemyY += enemyY_change
    
    player(playerX,playerY)
    Enemy(enemyX,enemyY)
    pygame.display.update()