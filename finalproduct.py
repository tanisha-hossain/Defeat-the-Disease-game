# Title: Defeat The Disease
# Names: Caitlin Chin, Tanisha Hossain
# Date: 22 January 2024
# Description:
# Our game is named Defeat The Disease, and we developed it for our culminating project in our Introduction to Computer Science course.
# It is based off of the game Angry Birds, with a new narrative and different characters and features.
# To play, read the first two introductory screens, which you can click through using the spacebar. After reading the narrative you will be directed to level 1.
# Drag the alien in the slingshot back and to fling it, release the mouse. The goal is to destroy all the enemies with the certain number of tries allotted for each level.
# If you run out of tries, you will lose a life an 250 points and have to try the level again. Try not to lose all your lives or the game ends!
# Some levels offer powerups and other levels offer you to choose an alien from various options.
# Good luck!


import pgzrun
from pgzhelper import * 
import os
import random


# Window Settings

os.environ['SDL_VIDEO_CENTERED'] = '1' #Forces window to be centered on screen.
WIDTH = 1025
HEIGHT = 700
BACKGROUND = 'colored_shroom' 
TITLE = "Defeat the Disease"


# INITIALIZE GLOBAL VARIABLES
SCORE = 0
LIVES = 3
BEST_SCORE = 0
tries = 0 #how many attempts a player gets in each level
page = 1
enemyStructure = []
enemies = []
playerIcons = []
powerup = None
multiplier = 0.08

# Booleans/Flags
alienDragged = False
released = False
flying = 0
alienIconSelected = False
lockIcons = False
gameStatus = 'playing'
actionOfPowerup = 'neutral'
doubledamage = False


# INITIALIZE PRIMARY ACTORS

# Main Actor: Alien 
playerAlien = Actor('alienyellow_round')
playerAlien.pos = (147, 442)
playerAlien.scale = 0.5 #resizing sprite to something more reasonable

playerAlien.images = ['alienyellow_round', "aliengreen_round", "alienblue_round"]

#Slingshot
slingshot = Actor('slingshot_angrybirds')
slingshot.pos = (140, 475)
slingshot.scale = 0.017 #resizing sprite to something more reasonable

# Left half of the slingshot (drawn over player's alien to make it more realistic when the alien passes through the slingshot)
slingshotLeft = Actor('slingshot_left')
slingshotLeft.pos = (133, 475)
slingshotLeft.scale = 0.077 #resizing sprite to something more reasonable

# Different alien options for player to choose from 
yellowAlien = (Actor('alienyellow_round', center= (100, 100)))
greenAlien = (Actor('aliengreen_round', center = (150, 100)))
blueAlien = (Actor("alienblue_round", center = (200, 100)))

      
# FUNCTIONS

# The load_page function is used to add all the components of each screen (start screens, levels, game over) depending on
# the page number. It switches the backgrounds between pages, and creates the different structures, enemy positions, and choice of players for each level.
# Additionally, the number of tries a player is given is set depending on the level, and powerups are called as a possibility for levels 3-5 (see generate_powerups() function)
def load_page(page_num):
    global BACKGROUND, yellowAlien, greenAlien, blueAlien, playerAlien, tries, doubledamage
    
    BACKGROUND = None
    playerIcons.clear()
    enemyStructure.clear ()
    enemies.clear ()
    doubledamage = False  #ensures that each time a new page is loaded, the 2x damage feature won't carry on unless set again


    # Title page
    if page_num == 1:
        BACKGROUND = "colored_land"
        music.play('backgroundmusic') # music plays from the beginning of the game, and resets when a new game starts


    # Narrative page
    if page_num == 2:
        BACKGROUND = "colored_land"


    #level 1    
    if page_num == 3:
        BACKGROUND = 'colored_shroom'
        enemies.clear()
        playerAlien.image = yellowAlien.image #set player automatically to the first choice in "choose your player" section
        playerIcons.append(yellowAlien) #choice of aliens
        yellowAlien.x = 100
        
        # create enemy structure for this level
        enemyStructure.append(Actor('elementstone012', center = (835, 475)))
        enemyStructure.append(Actor('elementstone012', center = (700, 585)))
        enemyStructure.append(Actor('elementwood019', center = (935, 500)))
        enemyStructure.append(Actor('elementwood016', center = (800, 575)))
        enemyStructure.append(Actor('elementwood013', center = (660, 650)))

        # add enemies to the level
        enemies.append(Actor('slimeblock', center = (935, 360)))
        enemies.append(Actor('slimeblock', center = (800, 410)))
        enemies.append(Actor('slimeblock', center = (660, 518)))

        # number of tries the player gets before failing the level
        tries = 5

                 
     # level 2   
    if page_num == 4:
        BACKGROUND = 'colored_grass'
        enemies.clear()
        playerAlien.image = greenAlien.image
        greenAlien.x = 100
        playerIcons.append(greenAlien)

        #structure
        enemyStructure.append(Actor('elementstone013', center = (675, 550)))
        enemyStructure.append(Actor('elementstone011', center = (525, 550)))
        enemyStructure.append(Actor('elementstone011', center = (825, 550)))
        enemyStructure.append(Actor('elementwood016', center = (525, 445)))
        enemyStructure.append(Actor('elementwood016', center = (825, 445)))
        enemyStructure.append(Actor('elementstone012', center = (675, 330)))

        #enemies
        enemies.append(Actor('slimeblock', center = (670, 480)))
        enemies.append(Actor('slimeblock', center = (825, 345)))
        enemies.append(Actor('slimeblock', center = (525, 345)))
        enemies.append(Actor('slimeblock', center = (670, 260)))

        #tries per level
        tries = 5
        
    
    # level 3    
    if page_num == 5:
        BACKGROUND = 'colored_desert'
        enemies.clear()
        playerAlien.image = yellowAlien.image
        yellowAlien.x = 100
        greenAlien.x = 150
        playerIcons.append(yellowAlien)
        playerIcons.append(greenAlien)

        #structure
        enemyStructure.append(Actor('elementwood016', center = (935, 550)))
        enemyStructure.append(Actor('elementwood016', center = (850, 550)))
        enemyStructure.append(Actor('elementwood016', center = (650, 550)))
        enemyStructure.append(Actor('elementwood016', center = (565, 550)))

        enemyStructure.append(Actor('elementstone013', center = (870, 450)))
        enemyStructure.append(Actor('elementstone013', center = (650, 450)))

        enemyStructure.append(Actor('elementwood016', center = (935, 350)))
        enemyStructure.append(Actor('elementwood016', center = (565, 350)))

        enemyStructure.append(Actor('elementstone013', center = (870, 250)))
        enemyStructure.append(Actor('elementstone013', center = (650, 250)))        

        #enemies
        enemies.append(Actor('slimeblock', center = (650, 383)))
        enemies.append(Actor('slimeblock', center = (750, 383)))
        enemies.append(Actor('slimeblock', center = (850, 383)))
        enemies.append(Actor('slimeblock', center = (750, 186)))

        #tries per level
        tries = 7

        # calls generate_powerups() functions because level 3 is one of the levels where the player has a chance to attain a powerup
        generate_powerups()


    # level 4
    if page_num == 6:
        BACKGROUND = 'colored_land'
        enemies.clear()
        playerAlien.image = greenAlien.image
        greenAlien.x = 100
        blueAlien.x = 150
        playerIcons.append(greenAlien)
        playerIcons.append(blueAlien)
        
        #structure
        enemyStructure.append(Actor('elementstone012', center = (870, 550)))
        enemyStructure.append(Actor('elementstone012', center = (520, 550)))
        enemyStructure.append(Actor('elementstone012', center = (720, 570)))

        enemyStructure.append(Actor('elementwood019', center = (935, 530)))
        enemyStructure.append(Actor('elementwood019', center = (810, 530)))
        
        enemyStructure.append(Actor('elementwood019', center = (585, 530)))
        enemyStructure.append(Actor('elementwood019', center = (460, 530)))
                              
        enemyStructure.append(Actor('elementwood016', center = (760, 600)))
        enemyStructure.append(Actor('elementwood016', center = (635, 600)))

        enemyStructure.append(Actor('elementstone013', center = (870, 400)))
        enemyStructure.append(Actor('elementstone013', center = (520, 400)))
        
        #enemies
        enemies.append(Actor('slimeblock', center = (870, 485)))
        enemies.append(Actor('slimeblock', center = (520, 485)))
        enemies.append(Actor('slimeblock', center = (870, 335)))
        enemies.append(Actor('slimeblock', center = (520, 335)))
        enemies.append(Actor('slimeblock', center = (700, 503)))

        #tries per level
        tries = 7

        # calls generate_powerups() functions because level 4 is one of the levels where the player has a chance to attain a powerup
        generate_powerups()


    # level 5
    if page_num == 7:
        BACKGROUND = 'colored_shroom'
        enemies.clear()
        playerAlien.image = yellowAlien.image
        yellowAlien.x = 100
        greenAlien.x = 150
        blueAlien.x = 200
        playerIcons.append(yellowAlien)
        playerIcons.append(greenAlien)
        playerIcons.append(blueAlien)

        #structure
        enemyStructure.append(Actor('elementstone012', center = (850, 620)))
        enemyStructure.append(Actor('elementstone034', center = (760, 475)))
        enemyStructure.append(Actor('elementstone034', center = (850, 325)))

        enemyStructure.append(Actor('elementstone020', center = (500, 500)))
        enemyStructure.append(Actor('elementwood019', center = (800, 550)))
        enemyStructure.append(Actor('elementwood019', center = (800, 330)))

        enemyStructure.append(Actor('elementstone012', center = (500, 630)))
        enemyStructure.append(Actor('elementstone012', center = (500, 400)))
        enemyStructure.append(Actor('elementstone011', center = (410, 400)))
        enemyStructure.append(Actor('elementstone011', center = (590, 400)))
        enemyStructure.append(Actor('elementstone011', center = (410, 630)))
        enemyStructure.append(Actor('elementstone011', center = (590, 630)))

        #enemies
        enemies.append(Actor('slimeblock', center = (870, 350)))
        enemies.append(Actor('slimeblock', center = (590, 563)))
        enemies.append(Actor('slimeblock', center = (870, 555)))
        enemies.append(Actor('slimeblock', center = (590, 335)))
        enemies.append(Actor('slimeblock', center = (735, 500)))
        
        enemies.append(Actor('slimeblock', center = (415, 335)))
        enemies.append(Actor('slimeblock', center = (415, 563)))
        enemies.append(Actor('slimeblock', center = (735, 373)))
        enemies.append(Actor('slimeblock', center = (870, 228)))

        #tries per level
        tries = 7

        # calls generate_powerups() functions because level 5 is one of the levels where the player has a chance to attain a powerup
        generate_powerups()


    # scaling alien icons in "Choose Your Alien" section
    for player in playerIcons:
        player.scale = 0.5
        
    # animating movement of bacteria enemies
    for enemy in enemies:
        enemy.fps = 2
        enemy.move_cycle = ['slimeblock', 'slimeblock_move']
        enemy.scale = 0.5


    
# The transition_screens() function checks the game status to know whether to pop up a message for the player and what the message would be.
# A pop up message appears whenever a level is completed or failed, or if the game has been lost or won.
def transition_screens():
    global gameStatus, page, screen, flying, lockIcons, SCORE, tries, LIVES, BEST_SCORE

    # if the player destroys all enemies and has finished flying, the level is complete, thus triggering the transition message which tells the player how to move to the next level 
    if page > 2 and page < 7:
        if len(enemies)==0 and flying == 0:
            gameStatus = 'levelcomplete'
            if gameStatus == 'levelcomplete':
                screen.draw.filled_rect(Rect(255, 175, 510, 200), color=(137, 219, 236))
                screen.draw.text("LEVEL COMPLETE", center = (512.5, 250), fontsize = 70, color = 'white')
                screen.draw.text("Press right arrow key to continue", center = (512.5, 325), fontsize = 25, color = 'white')


    # when all lives are lost, the status of the game switches to "game lost" which triggers the message that they lost with their final score and overall high score
    if LIVES < 1:
        gameStatus = 'gameLost'
        if gameStatus == 'gameLost':
            screen.draw.filled_rect(Rect(255, 175, 510, 220), color='red')
            screen.draw.text("YOU LOSE!", center = (512.5, 250), fontsize = 70, color = 'white')
            screen.draw.text(f"Your Score: {SCORE}    Best Score: {BEST_SCORE}", center = (512.5, 315), fontsize = 25, color = 'white')
            screen.draw.text("Press spacebar to return to start", center = (512.5, 335), fontsize = 25, color = 'white')


    # the player fails the level when they run out of tries and there are still enemies who haven't been destroyed
    if tries < 1 and len(enemies) > 0 and LIVES >= 1:
        gameStatus = 'levelFailed'
        if gameStatus == 'levelFailed':
            screen.draw.filled_rect(Rect(255, 175, 510, 200), color='red')
            screen.draw.text("LEVEL FAILED", center = (512.5, 250), fontsize = 70, color = 'white')
            screen.draw.text("Press left arrow key to replay level", center = (512.5, 325), fontsize = 25, color = 'white')


    # once the player completes level 5, they have completed the game and a message pops up with their final and highest score
    if page == 7 and len(enemies)==0 and flying == 0:
        gameStatus = 'gameWon'
        if gameStatus == 'gameWon':
            screen.draw.filled_rect(Rect(255, 175, 510, 220), color=(137, 219, 236))
            screen.draw.text("YOU WIN!", center = (512.5, 250), fontsize = 70, color = 'white')
            screen.draw.text(f"Your Score: {SCORE}    Best Score: {BEST_SCORE}", center = (512.5, 315), fontsize = 25, color = 'white')
            screen.draw.text("Press spacebar to return to start", center = (512.5, 335), fontsize = 25, color = 'white')



# As suggested by its name, this function assigns different attributed to the different aliens, such as how far it travels (see mouse up function)
# It also gives them different sizes.
def assign_alien_attributes():
    global greenAlien, yellowAlien, blueAlien, multiplier, playerAlien

    # yellow alien can travel at normal pace and is medium-sized
    if playerAlien.image == yellowAlien.image:
        multiplier = 0.06 # dictates how far the alien can travel in the mouse_up function
        playerAlien.scale = 0.5

    # green alien is small but fast
    if playerAlien.image == greenAlien.image:
        multiplier = 0.08
        playerAlien.scale = 0.4

    # blue alien is bigger but slower
    if playerAlien.image == blueAlien.image:
        multiplier = 0.04
        playerAlien.scale = 0.6



# This function removes a material from the structure or an enemy when the player collides with it. On collision, a sound is played
# and the player earns 10 points for hitting the structure and 20 points for hitting enemies.
def check_for_hit():
    global SCORE, powerup, LIVES, actionOfPowerup, doubledamage

    # removes materials and adds points when player hits them
    for material in enemyStructure:
        if playerAlien.colliderect(material):
            enemyStructure.remove(material)
            sounds.laser_002.play()

            # if the player has not hit the powerup that allows them to cause 2x damage, materials are worth 10 points.
            # but if the player has attained the 2x damage powerup, materials earn double of their usual points
            if doubledamage == False: 
                SCORE += 10
            else:
                SCORE += 20
                print('material worth 20') #just to ensure functionality

    # removes enemies and adds points when player hits them
    for enemy in enemies:
        if playerAlien.colliderect(enemy):
            enemies.remove(enemy)
            sounds.laser_002.play()

            # if the player has not hit the powerup that allows them to cause 2x damage, enemies are worth 20 points.
            # but if the player has attained the 2x damage powerup, enemies earn double of their usual points
            if doubledamage == False:
                SCORE += 20
            else:
                SCORE += 40 
                print('enemy worth 40') #just to ensure functionality

            

# This functions resets the player's alien in slingshot when it leaves the screen and notes that a try has been used each time the alien is reset.
def reset_alien():
    global alienDragged, released, powerup, flying, lockIcons, tries
    
    if playerAlien.x < 0 or playerAlien.x > WIDTH or playerAlien.y < 0 or playerAlien.y > HEIGHT:
        playerAlien.pos = (147, 442)
        alienDragged = False
        released = False
        flying = 0
        lockIcons = False
        tries -= 1



# Draws the characters shown on the narrative page. This function is only called during the narrative page, which explains how each element of the game works.
def start_screen_characters():
    disease = (Actor('slimeblock', center= (650,515)))
    disease.scale = 0.5

    stone = (Actor('elementstone011', center=(790, 525)))
    stone.scale = 0.5
    
    wood = (Actor('elementwood010', center= (840, 525)))
    wood.scale = 0.5
    
    alien1 = (Actor('alienyellow_round', center= (200, 525)))
    alien2 = (Actor('aliengreen_round', center = (350, 525)))
    alien3 = (Actor("alienblue_round", center = (500, 525)))
    
    alien1.draw()
    alien2.draw()
    alien3.draw()
    disease.draw()
    stone.draw()
    wood.draw()



# This function is called during levels 3-5. It randomly decides whether to make a powerup available for the player to collect or not.
# If a powerup is available, it is assigned a random action for it to perform--either a bonus life or doubele damage. It also appears in a random position.
def generate_powerups():
    global powerup, page, gameStatus, LIVES, SCORE, actionOfPowerup, doubledamage

    # ensures that each time the function is called, the availability and action of powerups are set back to an initial state
    availability = 'neutral'
    actionOfPowerup = 'neutral'

    # these lists provide options of types of powerups and whether it should be available or not
    powerupTypes = ['bonusLife', 'doubleDamage']
    availabilityOptions = ['available', 'unavailable']

    #randomly chooses whether powerups should be available and what type of powerup it would be
    availability = random.choice(availabilityOptions)
    actionOfPowerup = random.choice(powerupTypes)
    
    # if a powerup is deemed to be available, make it appear in a random position 
    if availability == 'available':
        powerup = (Actor('stargold'))
        powerup.x = random.randint(200, 600)
        powerup.y = random.randint(100, 500)
        print(1) #just to make sure the function is actually working
        
        # make sure an action is assigned to the powerups
        if actionOfPowerup == 'bonusLife':
            print('bonus life')

        else:
            print('2x damage')


    else:
        powerup = None
        print(9) #just to make sure the function is actually working



# This function dictates what happens when the player collects a powerup, depending on the type of powerup it is.
# If the powerup type is "bonus life" then the player gets an extra life and 250 points.
# If its a "double damage" powerup, the doubleDamage variable becomes true, which makes objects worth double their points in the check_for _hit() function
def powerup_results():
    global playerAlien, powerup, LIVES, SCORE, gameStatus, actionOfPowerup, doubledamage
    
    if powerup != None and playerAlien.colliderect(powerup):

        if actionOfPowerup == 'bonusLife':
            LIVES += 1
            SCORE += 250
            powerup = None
                
        if actionOfPowerup == 'doubleDamage' and gameStatus == 'playing':
            doubledamage = True #see check_for_hit() function
            # scales the powerup to practically invisible rather than making it a Nonetype just because it's complicated to remove the powerup while still having its function continue
            powerup.scale = 0.01

    
# This function sets the high score at the end of a game, comparing the player's score the overall higghest score they've achieved. 
def new_best_score():
    global BEST_SCORE, SCORE, gameStatus
    if gameStatus== 'gameLost' or gameStatus=='gameWon':
        if SCORE > BEST_SCORE:
            BEST_SCORE = SCORE



# When a new game begins(see key down function), variables are set to their initial state. 
def set_new_game():
    global SCORE, screen, page, LIVES, doubledamage, actionOfPowerup

    screen.clear()
    page = 1
    load_page(1)
    LIVES = 3
    SCORE = 0
    actionOfPowerup = 'neutral'
    doubledamage = 'false'



# This function controls what happens when certain keys on the keyboard are pressed, which are used to transition between pages.
def on_key_down(key, unicode):
    global page, gameStatus, flying, LIVES, SCORE

    # players have to click spacebar to move through the two start screens
    if key == keys.SPACE and page < 3:
        page += 1
        load_page(page)
        
    # when player completes a level, they have to click right arrow key to move to the next
    if page < 7 and page > 2:
        if key == keys.RIGHT and gameStatus == 'levelcomplete':
            page += 1
            load_page(page)
            gameStatus = 'playing'

    # when a player fails a level, they have to click the left arrow key to try again, but also lose a life and 250 points
    if key == keys.LEFT and gameStatus == 'levelFailed':
            load_page(page)
            gameStatus = 'playing'
            LIVES -= 1
            SCORE -= 250

    # when the game ends, the player has to click the spacebar to start a new game
    if key== keys.SPACE and (gameStatus == 'gameWon' or gameStatus == 'gameLost'):
        set_new_game()
        gameStatus = 'playing'

       

# This function controls what happens when the mouse is pressed down, specifically when selecting the type of alien to place in the slingshot
# and when the 
def on_mouse_down(pos,button):
    global playerAlien, alienDragged, alienIconSelected, yellowAlien, blueAlien, greenAlien, lockIcons, gameStatus

    if button==mouse.LEFT and gameStatus == 'playing':
        for icon in playerIcons:
            # switches the playerAlien to whatever alien is selected from icons in the top left corner
            if icon.collidepoint(pos) and lockIcons == False:
                playerAlien.image = icon.image
                alienIconSelected = True
                return
        
            else: 
                print("x:" + str(pos[0]) + ", y:" + str(pos[1])) #just to help with knowing coordinates of different elements

                if playerAlien.collidepoint(pos):
                    alienDragged = True


# This function controls what happens when the mouse is released 
def on_mouse_up(pos,button):
    global alienDragged, released, alienIconSelected, multiplier, flying, lockIcons, gameStatus 

    if button==mouse.LEFT and gameStatus == 'playing':
        if alienIconSelected==False:
            
            alteredPos = list(pos) #turning pos tuple into a list

            #checks position of mouse release, wont run alien movement if outside of bounds
            if alteredPos[0] <= 147 and alteredPos[1] >= 350:
                flying += 1
                alienDragged = False
                released = True
                sounds.slingnoise.play()

                if flying == 1: #makes sure nothing happens if the mouse is released behind the slingshot while the alien is already flying
                    lockIcons = True  #players can't change aliens while one is flying
                    x = pos[0]
                    y = pos[1]
                    #set the dx and dy values of the player alien based on its distance from the slingshot when released
                    playerAlien.dx = (slingshot.x - x)*multiplier
                    playerAlien.dy = (slingshot.top - y)*multiplier #multiplier is a variable used to moderate the speed of the alien reasonably (it also changes depending on the alien type)

        #resets on each mouse release
        alienIconSelected = False



# This function controls what happens as the mouse is moved, particularly while the mouse is also down to create a drag like motion.
def on_mouse_move(pos, rel, buttons):
    global alienDragged, gameStatus
    
    if gameStatus == 'playing' and (mouse.LEFT in buttons) and alienDragged==True:
                
        alteredPos = list(pos)#turning pos tuple into a list

        #ensures playerAlien is not moved out of bounds
        if alteredPos[0] > 147:
            alteredPos[0] = 147
        if alteredPos[1] < 350:
            alteredPos[1] = 350
                    
        playerAlien.pos = tuple(alteredPos) #turning alteredPos list back to tuple


    
# Update - Handle ongoing input, update positions, check interactions
def update():
    global released, alienDragged, page

    # ensurs the playerAlien never suddenly grows too big
    playerAlien.scale = 0.5

    # sets the alien in an arc like motion using the values of dx and dy from mouse up function
    if released==True:
        playerAlien.x += playerAlien.dx
        playerAlien.y += playerAlien.dy
        playerAlien.dy += 0.07 #gravity

    # animates and scales the enemies
    for enemy in enemies: 
        enemy.images = enemy.move_cycle
        enemy.scale = 0.5
        enemy.animate ()
        
    # functions that need to be called continuously
    check_for_hit()
    powerup_results()
    assign_alien_attributes()
    reset_alien()
    new_best_score()
    

# Draw - Draw each Actor, and any other UI elements
def draw():
    global slingshot, slingshotLeft, alienDragged, page, powerup, gameStatus
    
    screen.clear()
    screen.blit(BACKGROUND, (0,0))

    for icon in playerIcons: 
        icon.draw()  # draws the icons in the "Choose Your Alien" section
    
    for enemy in enemies:
        enemy.draw()
    
    for materials in enemyStructure:
        materials.draw()

    # Levels 2-4 don't have a mushroom for the slingshot to stand on, so a ledge substitutes for it
    if page > 3 and page <7:
        ledge = Actor('elementmetal013', center= (85, 540))
        ledge.scale = 0.85
        ledge.draw()  


    # When the player alien is being dragged, two lines are attached from the slingshot to the sides of the alien to depict the elastic band 
    if alienDragged == True: 
        screen.draw.line((153,433), playerAlien.midright, (110,38,14))
        screen.draw.line((132,437), playerAlien.midleft, (110,38,14))


    # Text on title screen
    if page == 1:
        screen.draw.text("Defeat the Disease", center = (512.5, 250), fontsize = 70, color = 'black')
        screen.draw.text("Press spacebar to start", center = (512.5, 325), fontsize = 25, color = 'black')


    # Draws text and characters for the second page which is the narrative screen
    if page == 2:
        screen.draw.text("Humans have brought a deadly disease to the alien’s planet. ", center = (512.5, 150), fontsize = 30, color = 'black')
        screen.draw.text("Help the aliens destroy the disease and their", center = (512.5, 200), fontsize = 30, color = 'black')
        screen.draw.text("hideout before they multiply and leave the alien planet uninhabitable.", center = (512.5, 250), fontsize = 30, color = 'black')
        screen.draw.text("There is a limited number of aliens willing to give their lives to the cause,", center = (512.5, 300), fontsize = 30, color = 'black')
        screen.draw.text("so the player cannot use the aliens recklessly—three strikes and they’re fired.", center = (512.5, 350), fontsize = 30, color = 'black')
        screen.draw.text("Press spacebar to save the world", center = (512.5, 425), fontsize = 25, color = 'black')
        
        start_screen_characters() # show images of the elements of the game
        
        screen.draw.text("Normal Alien", center= (200, 575), fontsize = 22, color = 'black')
        screen.draw.text('Fast Alien', center = (350, 575), fontsize = 22, color = 'black')
        screen.draw.text("Slow Alien", center = (500, 575), fontsize = 22, color = 'black')
        screen.draw.text("Disease: 20 points", center = (650, 575), fontsize = 22, color = 'black')
        screen.draw.text("Structure: 10 points", center = (810, 575), fontsize = 22, color = 'black')
        
        
   # For the game's levels, draw all the actors of the game and the text within it.      
    if page > 2:
        
        slingshot.draw()
        playerAlien.draw()
        slingshotLeft.draw()
    
        screen.draw.text(f"Level: {page - 2}", center = (512.5, 50), fontsize = 50, color = 'black')
        screen.draw.text(f"Best Score: {BEST_SCORE}", center = (WIDTH - 120, 50), fontsize = 25, color = 'black')
        screen.draw.text(f"Score: {SCORE}", center = (WIDTH - 120, 80), fontsize = 25, color = 'black')
        screen.draw.text(f"Lives: {LIVES}", center = (WIDTH - 120, 110), fontsize = 25, color = 'black')
        screen.draw.text("CHOOSE YOUR ALIEN:", center = (150, 50), fontsize = 25, color = 'black')

        transition_screens()

        screen.draw.text(f"Tries Left: {tries}", center = (75, 173), fontsize = 25, color = 'black')

    if powerup != None: 
        powerup.draw()


# Setup, Scheduling, and Go:
load_page(1)
pgzrun.go()
