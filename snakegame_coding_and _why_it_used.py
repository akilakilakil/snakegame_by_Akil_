#Snake Game 
import pygame #importing pygame module form using pygame inside the program
import sys#importing module to exiting the program
import random#importing module from randomly allocating snakefood
import time#importing time module for specific time after the gameover msg

# check for errors
check_errors = pygame.init()#initializing pygame straight forword
if check_errors[1] > 0:#the values of pygame.init was passed into check_error variable
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)#this module is used to exit the terminal
else:
    print("(+) PyGame successfully initialized!")
    spam=0
while spam<555:
    print("Akil.T,KGISL-IIM,Second year")
    print("")
    spam = spam+1

"""it will print had (0) initializating error if error occours
it will display PyGame successfully initialized! in the terminal""" 
# Play surface
playSurface = pygame.display.set_mode((720, 460))#setting the display size
pygame.display.set_caption('Snake game!')#giving title for snake game

# Colors
red = pygame.Color(255, 0, 0)  # gameover ,each values of colors are used rgb values
green = pygame.Color(0, 255, 0)  # snake,each values of colors are used rgb values
black = pygame.Color(0, 0, 0)  # score,each values of colors are used rgb values
white = pygame.Color(255, 255, 255)  # background,each values of colors are used rgb values
brown = pygame.Color(165, 42, 42)  # food,each values of colors are used rgb values

# Frames per second controller
fpsController = pygame.time.Clock()#using this we can control frame while running the program

#variables
snakePos = [100, 50]#x and y coordinate of snake to start
snakeBody = [[100, 50], [90, 50], [80, 50]]#3 blocks of the snake while the game starts

foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]#it will randomly generate the points in the screen revoluion of 720*460
foodSpawn = True#creating new food each time

direction = 'RIGHT'#used to change the direction
changeto = direction#assign to the variable changeto 

score = 0


# Game over function
def gameOver():
    myFont = pygame.font.SysFont('monaco', 72)#we are going to use default font in the system using system module name of the font and size should be declared
    GOsurf = myFont.render('Game over!', True, red)#this variable is created because of we should set the font to the pygame and enter the msg to be dispayed
    GOrect = GOsurf.get_rect()#this function going to get the rectangler function of the compount
    GOrect.midtop = (360, 15)#this function is used to display the game over msg in specipic position
    playSurface.blit(GOsurf, GOrect)#we are going to define that in player surface variale
    showScore(0)
    pygame.display.flip()#update the screen using this function

    time.sleep(4)#it will hold the gameover screen for 4 seconds
    pygame.quit()  # pygame exit
    sys.exit()  # terminal exit


def showScore(choice=1):
    sFont = pygame.font.SysFont('monaco', 24)
    Ssurf = sFont.render('Score : {0}'.format(score), True, black)
    Srect = Ssurf.get_rect()
    if choice == 1:
        Srect.midtop = (80, 10)
    else:
        Srect.midtop = (360, 120)
    playSurface.blit(Ssurf, Srect)


#direction of the keys we are going to use game
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                changeto = 'LEFT'
            if event.key == pygame.K_UP or event.key == ord('w'):
                changeto = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
#verifying the direction
    if changeto == 'RIGHT' and not direction == 'LEFT':
        direction = 'RIGHT'
    if changeto == 'LEFT' and not direction == 'RIGHT':
        direction = 'LEFT'
    if changeto == 'UP' and not direction == 'DOWN':
        direction = 'UP'
    if changeto == 'DOWN' and not direction == 'UP':
        direction = 'DOWN'
#Updating snake position 
    if direction == 'RIGHT':
        snakePos[0] += 10
    if direction == 'LEFT':
        snakePos[0] -= 10
    if direction == 'UP':
        snakePos[1] -= 10
    if direction == 'DOWN':
        snakePos[1] += 10

#Snake body adds when collecting food
    snakeBody.insert(0, list(snakePos))
    if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
        score += 1
        foodSpawn = False
    else:
        snakeBody.pop()

#Food Spawn
    if foodSpawn == False:
        foodPos = [random.randrange(1, 72) * 10, random.randrange(1, 46) * 10]
    foodSpawn = True

#Background
    playSurface.fill(white)

#Draw Snake
    for pos in snakeBody:
        pygame.draw.rect(playSurface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    pygame.draw.rect(playSurface, brown, pygame.Rect(foodPos[0], foodPos[1], 10, 10))

#gamever msg to be displayed
    if snakePos[0] > 710 or snakePos[0] < 0:
        gameOver()
    if snakePos[1] > 450 or snakePos[1] < 0:
        gameOver()

# if it hit in its own body
    for block in snakeBody[1:]:
        if snakePos[0] == block[0] and snakePos[1] == block[1]:
            gameOver()


    showScore()
    pygame.display.flip()

    fpsController.tick(15)#calling the functions,tick value declares the snake speed
########################################################################################################
    #########################--------By------Akil.T-----------------####################################
    ########################---------KGISL-IIM----------------------####################################
    ########################----------second year--------------------###################################
    ####################################################################################################

while True:
    print("Akil.T,KGISL-IIM,Second year")
