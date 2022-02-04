import pygame
import random

#Initialze the pygame
pygame.init()


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
enemyIMG = pygame.image.load('invader2.png')
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.2
enemyY_change = 32

#places enemy on the screen
def enemy(x,y):
    screen.blit(enemyIMG, (x, y))


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
    if enemyX <=0:
        enemyX_change =  .2
        enemyY += enemyY_change
    elif enemyX >= 750:
        enemyX_change = -.2
        enemyY += enemyY_change
    

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
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)
                
        
        #checking if key is taken up
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0
    
    
    


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    
    #moves player's x cordanite
    playerX += playerX_change
    enemyX += enemyX_change
    
    pygame.display.update()