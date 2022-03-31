import pygame
import random
import math

from pygame import mixer


#Initialze the pygame
pygame.init()

#Score

score_value =0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

def show_score(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x,y))


#backgroud Sound

#mixer.music.load('background.wav')
#mixer.music.play(-1)


#create screen
screen = pygame.display.set_mode((800, 600))

#adding background
background = pygame.image.load('background.jpg')

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon  = pygame.image.load('invader.png')
pygame.display.set_icon(icon)


######

#player
playerIMG = pygame.image.load('player2.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0


#places player on the screen
def player(x,y):
    screen.blit(playerIMG, (x, y))

####

#Enemy
enemyIMG = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6


for i in range(num_of_enemies):
    enemyIMG.append(pygame.image.load('invader2.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.2)
    enemyY_change.append(32)

#places enemy on the screen
def enemy(x,y, i):
    screen.blit(enemyIMG[i], (x, y))


#Bullet

bulletIMG = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 1
bullet_state = 'ready'  #ready means you cannot see the bullet
                        #fire mean the bullet is moving in the Y direction


#firing the bullet
def fire_bullet(x,y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bulletIMG, (x+16,y+10))


#collision detection
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt(math.pow(enemyX-bulletX, 2) + math.pow(enemyY-bulletY, 2))
    if distance < 20:
        return True
    else:
        return False
    

#game over Text
over_font = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
    over_text = over_font.render('GAME OVER', True, (255, 255, 255))
    screen.blit(over_text, (200, 250))



#game is over when it hits an area

######

#events are anything happening in the game window
#GAME Loop where everything must happen.
running = True

while running:

    #screen color RGB 0-255
    screen.fill((0,0,0))
    #Background image
    screen.blit(background, (0,0))

    #defining the boundry of the spaceship
    if playerX <=0:
        playerX = 0
    elif playerX >= 750:
        playerX = 750


    #defining the boundry of the enemy
    for i in range(num_of_enemies):  
        enemyX[i] += enemyX_change[i]

        if enemyX[i] <=0:
            enemyX_change[i] =  .2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 750:
            enemyX_change[i] = -.2
            enemyY[i] += enemyY_change[i]
    #COllision
        collision =isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        
        if collision:
            bulletY =480
            bullet_state = 'ready'
            score_value += 1
            
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
            #explosion_sound = mixer.Sound('explosion.wav')
            #explosion_sound.play()
        
        enemy(enemyX[i], enemyY[i], i)

        # Game Over

        if enemyY[i] > 450:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break

            #print("Game Over")
            #running = False





    #bullet movment
    if bulletY == 0:
        bulletY =480
        bullet_state = 'ready'
    
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    




    #defining when the enemy hits the game over screen



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #adding key stroke pressing right or left
        if event.type == pygame.KEYDOWN: #KEYDOWN checks if a key is pressed
           
            if event.key == pygame.K_LEFT:
                playerX_change =-.8
                
            if event.key == pygame.K_RIGHT:
                playerX_change = .8
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    #bullet_sound = mixer.Sound('laser.wav')
                    #bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        
        #checking if key is taken up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0
    
    
    

        
    


    player(playerX, playerY)
    show_score(textX, textY)
    
    #moves player's x cordanite
    playerX += playerX_change
    
    
    pygame.display.update()