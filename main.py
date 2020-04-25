import math
import random

import pygame
from pygame import mixer

# Intialize the pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((540, 540))

# Background
background = pygame.image.load('background.jpg')

# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)

# Caption and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('bullet.png')
pygame.display.set_icon(icon)

# Player

playerImg = pygame.image.load('player.png')
playerX = 370
playerY = 450
playerX_change = 0


# Enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(i*100)
    enemyY.append(0)
    enemyX_change.append(-1)
    enemyY_change.append(40)
#Enemy 2
enemyImg2 = []
enemyA = []
enemyB = []
enemyA_change = []
enemyB_change = []
num_of_enemies = 4

for i in range(num_of_enemies):
    enemyImg2.append(pygame.image.load('enemy2.png'))
    enemyA.append(i*100)
    enemyB.append(0)
    enemyA_change.append(-.45)
    enemyB_change.append(50)
# Bullet

# Ready - You can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"

#colors 

red = (200,0,0)
yellow = (200,200,0)
light_yellow = (255,255,0)
light_red = (255,0,0)

# Score

score_value = 0
font = pygame.font.Font('browsercyberlinknew.ttf', 32)

textX = 10
testY = 10

# Game Over
over_font = pygame.font.Font('browsercyberlinknew.ttf', 64)

# intro screen 
intro_font = pygame.font.Font('browsercyberlinknew.ttf', 30)

def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (100, 150))

def final_score_text():
    score_text = over_font.render(" SCORE: " + str(score_value), True, (149, 132, 210))
    screen.blit(score_text, (100, 250))

def game_intro_text():
    WHITE=(0,0,0)
    pygame.draw.rect(screen,WHITE,(100,90,330,350))
    intro_text = over_font.render("INVADERS", True, (203, 195, 232))
    screen.blit(intro_text, (123, 100))
    enemy_img=pygame.image.load('enemy.png') 
    screen.blit(enemy_img,(130,200))
    point_text = font.render(" - 1 point", True, (255, 255, 255))
    screen.blit(point_text, (200, 220))
    enemy_two=pygame.image.load('enemy2.png') 
    screen.blit(enemy_two,(130,300))
    point2_text = font.render(" - 2 points", True, (203, 195, 232))
    screen.blit(point2_text, (200, 320))
    start_text = intro_font.render("Hit space to play ", True, (255, 255, 255))
    screen.blit(start_text, (123, 400))
def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

def enemy2(x, y, i):
    screen.blit(enemyImg2[i], (x, y))



def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX - bulletX, 2) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def isCollisiontwo(enemyA, enemyB, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyA - bulletX, 2) + (math.pow(enemyB - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

def danger():
    danger_text = over_font.render("WATCH OUT!!", True, (255, 255, 255))
    screen.blit(danger_text, (120, 200))    
        

running = False 
while not running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  #key 1
                running = True
        game_intro_text()
        pygame.display.update() 
while running:
    # RGB = Red, Green, Blue
    screen.fill((0, 0, 0))
    # Background Image
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bulletSound = mixer.Sound("laser.wav")
                    bulletSound.play()
                    # Get the current x cordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    # 5 = 5 + -0.1 -> 5 = 5 - 0.1
    # 5 = 5 + 0.1

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Enemy Movement
    game_over = False
    danger_warning = False
    for i in range(num_of_enemies):
        if enemyY[i] > 350:
            danger_warning = True
        elif game_over == True:
            danger_warning = False
            
        if enemyB[i] > 350:
            danger_warning = True
        elif game_over == True:
            danger_warning = False
        # Game Over
        if enemyY[i] > playerY:
            for j in range(num_of_enemies):
                danger_warning = False
                game_over = True
                enemyY[j] = 2000
                enemyB[j] = 2000
                game_over_text()
                final_score_text()
                break
        elif enemyB[i] > playerY:
            for j in range(num_of_enemies):
                danger_warning = False
                game_over = True
                enemyY[j] = 2000
                enemyB[j] = 2000
                game_over_text()
                final_score_text()
                break
        if game_over == False: 
            enemyX[i] += enemyX_change[i]
            enemyA[i] += enemyA_change[i]
            if enemyX[i] and enemyA[i] <= 0:
                enemyX_change[i] = 4
                enemyA_change[i] = 4
                enemyY[i] += enemyY_change[i]
                enemyB[i] += enemyB_change[i]
                break
            elif enemyX[i] and enemyA[i] >= 736:
                enemyA_change[i] = -4
                enemyX_change[i] = -4
                enemyY[i] += enemyY_change[i]
                enemyB[i] += enemyB_change[i]
                break

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        collision2 = isCollisiontwo(enemyA[i], enemyB[i], bulletX, bulletY)
        if game_over == False:
            if collision:
                explosionSound = mixer.Sound("boom1.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 1
                enemyX[i] = ((i + 1) *100)
                enemyY[i] = (0)
            if collision2:
                explosionSound = mixer.Sound("boom8.wav")
                explosionSound.play()
                bulletY = 480
                bullet_state = "ready"
                score_value += 2
                enemyA[i] = random.randint(0, 540)
                enemyB[i] = random.randint(50, 200)
        enemy2(enemyA[i], enemyB[i], i)
        enemy(enemyX[i], enemyY[i], i)
        
    if danger_warning == True:
        danger()

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX, testY)
    pygame.display.update()
