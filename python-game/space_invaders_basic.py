import pygame
import random
import math
from pygame import mixer

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((800,600)) 

# Background
background = pygame.image.load('D:\\My-stuff\\python-game\\images\\background.png')

#Background sound
mixer.music.load('D:\\My-stuff\\python-game\\images\\background.wav')
mixer.music.play(-1)

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
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append( pygame.image.load('D:\\My-stuff\\python-game\\images\\alien.png'))
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(4)
    enemyY_change.append( 40)

# Bullet
# Ready - You can't see the bullet on the screen
# Fire -  The bullet is currently moving
bulletImg = pygame.image.load('D:\\My-stuff\\python-game\\images\\bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"


# Score

score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

def show_score(x,y):
    score = font.render("score :" +str(score_value), True, (255,255,255))
    screen.blit(score,(x,y))

#Game over text
over_font = pygame.font.Font('freesansbold.ttf',64) 

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text,(200,250))


def player(x,y):
    screen.blit(playerImg, (x, y))

def Enemy(x,y,i):
    screen.blit(enemyImg[i], (x, y))

def Bullet_fire(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2) + math.pow(enemyY-bulletY,2)))
    if distance <27 :
        return True
    else:
        return False
    


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

            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('D:\\My-stuff\\python-game\\images\\laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    Bullet_fire(bulletX,bulletY)


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
    for i in range(num_of_enemies):

        #Game over
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 4
            enemyY[i] += enemyY_change[i] 
        elif enemyX[i] >= 736:
            enemyX_change[i] = -4
            enemyY[i] += enemyY_change[i]
        
        #Collision
        collision = isCollision(enemyX[i],enemyY[i],bulletX,bulletY)
    
        if collision : 
            explosion_sound = mixer.Sound('D:\\My-stuff\\python-game\\images\\explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state ="ready"
            score_value += 1
            
            enemyX[i] = random.randint(0,736)
            enemyY[i] = random.randint(50,150)
        
        Enemy(enemyX[i],enemyY[i], i)
    
    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        Bullet_fire(bulletX,bulletY)
        bulletY -= bulletY_change
    



    player(playerX,playerY)
    show_score(textX,textY)
    pygame.display.update()

