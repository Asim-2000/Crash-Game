
import pygame, sys
import random
import time
clock = pygame.time.Clock()

pygame.init()

#VARIABLES
jump=0
life=1
multiplier=0
score=0
dodged=0
accelerate = 0
coinHeight=56
coinWidth=56

#XXXXXXXXXXXXXXXXXXX


y=0


obStart_y=-750
obStart_x=random.randrange(125,(675-62))


coinSpeed = 2                            # COIN
coinStart_y=-10000
coinStart_x=random.randrange(125,(675-56))
coins = pygame.image.load("coin.png")

lifeSpeed=2                              #LIFE    
LifeStart_y=-6200
LifeStart_x=random.randrange(125,(675-56))
life_pic=pygame.image.load("life.png")
                                            #NITROUS
AccSpeed=2
AccStart_y=-10000
AccStart_x=random.randrange(125,(675-56))
Acc_pic=pygame.image.load("jump.png")
#XXXXXXXXXXXXXXXXXXX

#IMAGES
background1 = pygame.image.load('grass.jpg')
intro_background = pygame.image.load("intro.jpg")
instruction_background = pygame.image.load("instruction.jpg")

car_image = pygame.image.load('car1.png')

userCar1 = pygame.image.load("userCar1.png")
userCar2 = pygame.image.load("userCar2.png")

roadTrack = pygame.image.load("track1.jpg")
desertTrack = pygame.image.load("track2.png")
menuRoadTrack = pygame.image.load("menuRoadTrack.jpg")
menuDesertTrack = pygame.image.load("menuDesertTrack.png")

#def userCar1Func():
#    gameDisplay.blit(userCar1,(lead_x,lead_y))
#def userCar2Func():    
#   gameDisplay.blit(userCar2,(lead_x,lead_y))

coins = pygame.image.load("coin.png")

#DISPLAY
displayWidth = 800
displayHeight = 600
gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
gameDislpay = pygame.display.set_caption('The Crash')

lead_x = displayWidth*0.45
lead_y = displayHeight*0.77

#COLOURS
white = (255, 255, 255)
red = (200, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
black = (0,0,0)
yellow =(225, 230, 0)
grey = (160, 160, 160)
skyblue = (55, 255, 255)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)
bright_blue = (0, 0, 255)
bright_grey = (192, 192, 192)
bright_yellow = (225, 250, 0)
bright_skyblue = (155, 255, 255)

#FUNCTION LIST
# 1. INTRO LOOP
# 2. BUTTON
# 3. INTRODUCTION
# 4. MODE
# 5. PAUSED
# 6. UNPAUSED
# 7. OBSTACLES
# 8. SCORING
# 9. TEXT OBJECTS 
# 10. MESSAGE DISPLAY
# 11. CRASH
# 12. BACKGROUND
# 13. CAR
# 14. GAME LOOP



    
        
    #crash

        
def intro_loop():
    pygame.mixer.music.load("music/atlanta.wav")
    pygame.mixer.music.play(-1)
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(intro_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 115)
        TextSurf, TextRect = text_objects("THE CRASH", largetext)
        TextRect.center = (400, 80)
        gameDisplay.blit(TextSurf, TextRect)
        button("START", 150, 500, 100, 50, green, bright_green, "start")
        button("QUIT", 550, 500, 100, 50, red, bright_red, "quit")
        button("INSTRUCTION", 300, 500, 200, 50, blue, bright_blue, "intro")
        pygame.display.update()
        clock.tick(50)

def introduction():
    introduction = True
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.blit(instruction_background, (0, 0))
        largetext = pygame.font.Font("freesansbold.ttf", 80)
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        mediumtext = pygame.font.Font("freesansbold.ttf", 40)
        textSurf, textRect = text_objects("This is a car game in which player will be dodging cars", smalltext)
        textRect.center = ((350), (200))
        TextSurf, TextRect = text_objects("INSTRUCTION", largetext)
        TextRect.center = ((400),(100))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(textSurf, textRect)
        sTextSurf, sTextRect = text_objects("CONTROLS", mediumtext)
        sTextRect.center = ((190),(250))
        rtextSurf, rtextRect = text_objects("ARROW UP: MOVE UPWARD", smalltext)
        rtextRect = ((80),(300))
        ptextSurf, ptextRect = text_objects("ARROW DOWN: MOVE DOWNWARD", smalltext)
        ptextRect = ((80),(350))
        stextSurf, stextRect = text_objects("ARROW LEFT: LEFT TURN", smalltext)
        stextRect = ((80),(400))
        hTextSurf, hTextRect = text_objects("ARROW RIGHT: RIGHT TURN", smalltext)
        hTextRect = ((80),(450))
        atextSurf, atextRect = text_objects("SPACE: ACTIVATE NITROUS", smalltext)
        atextRect = ((80),(500))
        gameDisplay.blit(sTextSurf, sTextRect)
        gameDisplay.blit(stextSurf, stextRect)
        gameDisplay.blit(hTextSurf, hTextRect)
        gameDisplay.blit(atextSurf, atextRect)
        gameDisplay.blit(rtextSurf, rtextRect)
        gameDisplay.blit(ptextSurf, ptextRect)
        button("BACK", 660, 500, 100, 50, blue, bright_blue, "backFromIntroduction")
        pygame.display.update()
        clock.tick(30)
        
def mode():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(instruction_background, (0,0))
        largetext = pygame.font.Font("freesansbold.ttf", 100)
        TextSurf, TextRect = text_objects("Choose Level", largetext)
        TextRect.center = ((displayWidth/2), ((displayHeight/2)-100))
        gameDisplay.blit(TextSurf, TextRect)
        button("EASY",150,350,100,50,green,bright_green,"easy")
        button("MEDIUM",350,350,100,50,blue,bright_blue,"medium")
        button("HARD",550,350,100,50,red,bright_red,"hard")
        button("BACK", 660, 500, 100, 50, blue, bright_blue, "backFromMode")
        pygame.display.update()
        clock.tick(30)
        
def cars():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(instruction_background, (0,0))
        largetext = pygame.font.Font("freesansbold.ttf", 40)
        TextSurf, TextRect = text_objects("Choose car by pressing button", largetext)
        TextRect.center = ((displayWidth/2), ((displayHeight/2)-200))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(userCar1, (215, 262))
        gameDisplay.blit(userCar2, (410, 262))
        button("CAR 1",200,400,100,50,green,bright_green,"car1")
        button("CAR 2",400,400,100,50, yellow, bright_yellow, "car2")
        button("BACK", 560, 450, 100, 50, blue, bright_blue, "backFromCars")
        pygame.display.update()
        clock.tick(30)

def tracks():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        gameDisplay.blit(instruction_background, (0,0))
        largetext = pygame.font.Font("freesansbold.ttf", 40)
        TextSurf, TextRect = text_objects("Choose track by pressing button", largetext)
        TextRect.center = ((displayWidth/2), ((displayHeight/2)-200))
        gameDisplay.blit(TextSurf, TextRect)
        gameDisplay.blit(menuRoadTrack, (250, 250))
        gameDisplay.blit(menuDesertTrack, (450, 250))
        button("Road",260,450,100,50,green,bright_green,"roadTrack")
        button("Desert",460,450,100,50, yellow, bright_yellow, "desertTrack")
        button("BACK", 660, 440, 100, 50, blue, bright_blue, "backFromTracks")
        pygame.display.update()
        clock.tick(30)

def button(msg, x, y, w, h, ic, ac, action = None):
    global car_image, background1
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if  x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1 and action != None:
            if action == "start":
                cars()
            elif action == "quit":
                pygame.quit()
                sys.exit()
            elif action == "intro":
                introduction()
            elif action == "backFromIntroduction":
                intro_loop()
            elif action == "car1":
                car_image = userCar1
                tracks()
            elif action == "car2":
                car_image = userCar2
                tracks()
            elif action == "backFromCars":
                intro_loop()
            elif action == "roadTrack":
                background1 = roadTrack
                mode()
            elif action == "desertTrack":
                background1 = desertTrack
                mode()
            elif action == "backFromTracks":
                cars()
            elif action == "easy":
                game_loop_EASY()
            elif action == "medium":
                game_loop_MEDIUM()
            elif action == "hard":
                game_loop_HARD()
            elif action == "backFromMode":
                tracks()
            elif action == "pause":
                paused()
            elif action == "unpause":
                unpaused()
            
            
                
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))
        smalltext = pygame.font.Font("freesansbold.ttf", 20)
        textsurf, textrect = text_objects(msg, smalltext)
        textrect.center = ((x + (w/2)), (y + (h/2)))
        gameDisplay.blit(textsurf, textrect)                

def text_objects(text,font) :
    textSurface = font.render(text,True,black)
    return textSurface,textSurface.get_rect()

def msg(text):
    largetext = pygame.font.Font("freesansbold.ttf",115)
    TextSurf , TextRect = text_objects(text,largetext)
    TextRect.center = ((displayWidth / 2), (displayHeight / 2))
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)    

def game_loop_EASY():
        pygame.mixer.music.load('music/coffee_stains.wav')
        pygame.mixer.music.play(-1)
        global pause, LifeStart_x,LifeStart_y,AccStart_x,AccStart_y,accelerate,lead_x,lead_y, white
        pygame.init()
        displayWidth = 800
        displayHeight = 600

        gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
        gameDislpay = pygame.display.set_caption('The Crash')

        coins = pygame.image.load('coin.png')



        coinHeight=56
        coinWidth=56


        jump=0
        life=1
        multiplier=0
        score=0
        dodged=0
        

        y=0

        obSpeed = 7
        obStart_y=-750
        obStart_x=random.randrange(125,(675-62))

        coinSpeed = 2
        coinStart_y=-1500
        coinStart_x=random.randrange(125,(675-56))
        button = ("PAUSE", 650, 0,  150, 50, green, bright_green, "pause")
        def coin(coinStart_x,coinStart_y):
            gameDisplay.blit(coins,(coinStart_x,coinStart_y))

        def crash(lead_x,lead_y):
            car_crash = pygame.image.load('carcrash.png')
            gameDisplay.blit(car_crash, (obStart_x-50,obStart_y+100))
            crash_sound = pygame.mixer.Sound("music/crash.wav")
            pygame.mixer.Sound.play(crash_sound)
            msg("You Crashed!!")
            pygame.mixer.music.stop()    


        
        def scoring(dodged,score,obSpeed,multiplier):
            font = pygame.font.SysFont(None,30)
            text = font.render("Cars Dodged "+str(dodged),True,black)
            scores = font.render("Score "+str(score),True,red)
            multiplier_count=font.render("Multiplier "+str(multiplier),True,black)
            life_count=font.render("Lives "+str(life),True,black)
            Acc_count=font.render("Nitrous "+str(accelerate),True,black)
            
            gameDisplay.blit(text,(10,50))
            gameDisplay.blit(scores,(10,20))
            gameDisplay.blit(multiplier_count,(10,80))
            gameDisplay.blit(life_count,(10,110))
            gameDisplay.blit(Acc_count,(10,140))

        def coin(coinStart_x,coinStart_y):
            gameDisplay.blit(coins,(coinStart_x,coinStart_y))

        def Life(LifeStart_x,LifeStart_y):
            gameDisplay.blit(life_pic,(LifeStart_x,LifeStart_y))

        def Acc(AccStart_x,AccStart_y):
            gameDisplay.blit(Acc_pic,(AccStart_x,AccStart_y))    

        def text_objects(text,font) :
            textSurface = font.render(text,True,black)
            return textSurface,textSurface.get_rect()
        def msg(text) :
            largetext = pygame.font.Font("freesansbold.ttf",115)
            TextSurf , TextRect = text_objects(text,largetext)
            TextRect.center = ((displayWidth / 2), (displayHeight / 2))
            gameDisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            time.sleep(2)
        def end () :
            msg("You Crashed")

            

              
            
        carWidth=62
        carHeight=128

        ob_width=64
        ob_height=128

        lead_x_change = 0
        lead_y_change = 0

        def background():
            gameDisplay.blit(background,(0,0))
            
        carDistance = 444

        #Scores
        passed = 0
        score = 0
        level=0

        def userCar1Func():
            gameDisplay.blit(userCar1,(lead_x,lead_y))
        def userCar2Func():    
            gameDisplay.blit(userCar2,(lead_x,lead_y))

        

        def car(lead_x,lead_y):
            gameDisplay.blit(car_image,(lead_x,lead_y))


        def obstacle1(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob1.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle2(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob2.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle3(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob3.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle4(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob4.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle5(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob5.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))    
            

        carDistance=800-(ob_height+carHeight)    
        roadWidth = 423
        obRightCorner=obStart_x+64
        obLeftCorner=obStart_x
           
        gameExit = False
        while not gameExit:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        lead_x_change+=3
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        lead_x_change -=3
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        lead_y_change =+1
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        lead_y_change -=1
                    if accelerate!=0:
                        if event.key == pygame.K_SPACE:
                            obSpeed+=4.5
                        
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d :
                    lead_x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    lead_y_change = 0
            if event.type == pygame.KEYUP:
                if accelerate!=0:
                    if event.key == pygame.K_SPACE:
                        obSpeed=7
                        accelerate-=1
            if lead_x<125 or lead_x>(675-62):#car width = 62
                life=life-1
                if life==0:
                    end()
                    pygame.quit()

            pause = True
            if multiplier==0:
                if obStart_y>displayHeight:
                    obStart_y=0-ob_height
                    obStart_x=random.randrange(125,(675-64))
                    score+=10
                    dodged+=1
                    if dodged%10==0:
                        level+=1
                        obSpeed+=4.5
                        msg("Level "+str(level))              
            elif multiplier!=0:
                if obStart_y>displayHeight:
                    obStart_y=0-ob_height
                    obStart_x=random.randrange(125,(675-64))
                    score+=20
                    dodged+=1
                    multiplier-=1
                    if dodged%10==0:
                        level+=1
                        obSpeed+=4.5
                        msg("Level "+str(level))

                
            

            if coinStart_y > displayHeight:
                coinStart_y = -15000
                coinStart_x = random.randrange(125,(675-56))

            if (coinStart_y+coinHeight)> lead_y:
                if lead_x > coinStart_x and lead_x < (coinStart_x + coinWidth) or (lead_x + carWidth) > coinStart_x and (lead_x + carWidth) < (coinStart_x + coinWidth):
                    coinStart_y=-6200 
                    multiplier+=1

            if (LifeStart_y+coinHeight)> lead_y:
                if lead_x > LifeStart_x and lead_x < (LifeStart_x + coinWidth) or (lead_x + carWidth) > LifeStart_x and (lead_x + carWidth) < (LifeStart_x + coinWidth):
                    LifeStart_y=-15000
                    life+=1       

            if LifeStart_y > displayHeight:
                LifeStart_y =-15000
                LifeStart_x = random.randrange(125,(675-56))

            if (AccStart_y+coinHeight)> lead_y:
                if lead_x > AccStart_x and lead_x < (AccStart_x + coinWidth) or (lead_x + carWidth) > AccStart_x and (lead_x + carWidth) < (AccStart_x + coinWidth):
                    AccStart_y=-15000
                    accelerate+=1       

            if AccStart_y > displayHeight:
                AccStart_y =-15000
                AccStart_x = random.randrange(125,(675-56))
                
            
            if lead_x<125 or lead_x>(675-62):#car width = 62
                life=life-1
                lead_x = displayWidth*0.45
                lead_y = displayHeight*0.7
                if life==0:
                    crash(lead_x,lead_y)
                    
                    intro_loop()

            if (obStart_y+ob_height)> lead_y:
                if lead_x > obStart_x and lead_x < (obStart_x + ob_width) or (lead_x + carWidth) > obStart_x and (lead_x + carWidth) < (obStart_x + ob_width):
                    life=life-1
                    lead_x = displayWidth*0.45
                    lead_y = displayHeight*0.77
                    if life==0:
                        crash(lead_x,lead_y)
                        
                        intro_loop()

            pause = True         
            lead_x += lead_x_change
            lead_y += lead_y_change
            gameDisplay.fill(white)
          
            
            rel_y = y % background1.get_rect().width
            gameDisplay.blit(background1,(0,rel_y-background1.get_rect().width))
            y+=obSpeed
            if rel_y < 800:
                gameDisplay.blit(background1,(0,rel_y))
            
            obStart_y-=(obSpeed/4)
            
            obStart_y+=obSpeed

            ob = random.randrange(0,3)
            if dodged%3==0:
                obstacle1(obStart_x,obStart_y)
            elif dodged%3==1:
                obstacle2(obStart_x,obStart_y)
            elif dodged%3==2:
                obstacle3(obStart_x,obStart_y)
            elif dodged%2==0:
                obstacle4(obStart_x,obStart_y)

            coinStart_y-=(obSpeed/4)
            coin(coinStart_x,coinStart_y)
            coinStart_y+=obSpeed
            
            LifeStart_y-=(obSpeed/4)
            Life(LifeStart_x,LifeStart_y)
            LifeStart_y+=obSpeed
                         
            AccStart_y-=(obSpeed/4)
            Acc(AccStart_x,AccStart_y)
            AccStart_y+=obSpeed
            
            
            #score_system(dodged,score,multiplier,life,jump)

            #firstCar = userCar1Func()
            #secondCar = userCar2Func()
            car(lead_x,lead_y)
            

            

            scoring(dodged,score,obSpeed,multiplier)
            #clock.tick(60)
            pygame.display.update()            
        pygame.quit()
        quit()
        game_loop()



#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX        
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX


def game_loop_MEDIUM():
        pygame.mixer.music.load('music/coffee_stains.wav')
        pygame.mixer.music.play(-1)
        global LifeStart_x,LifeStart_y,AccStart_x,AccStart_y,accelerate,lead_x,lead_y
        pygame.init()
        displayWidth = 800
        displayHeight = 600

        gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
        gameDislpay = pygame.display.set_caption('The Crash')

        #car_image = pygame.image.load('car1.png')
        #background = pygame.image.load('grass.jpg')
        coins = pygame.image.load('coin.png')



        coinHeight=56
        coinWidth=56


        jump=0
        life=1
        multiplier=0
        score=0
        dodged=0
        

        y=0

        obSpeed =9
        obStart_y=-750
        obStart_x=random.randrange(125,(675-62))

        coinSpeed = 2
        coinStart_y=-1500
        coinStart_x=random.randrange(125,(675-56))
        
        def coin(coinStart_x,coinStart_y):
            gameDisplay.blit(coins,(coinStart_x,coinStart_y))

        def crash(lead_x,lead_y):
            car_crash = pygame.image.load('carcrash.png')
            gameDisplay.blit(car_crash, (obStart_x,obStart_y+100))
            crash_sound = pygame.mixer.Sound("music/crash.wav")
            pygame.mixer.Sound.play(crash_sound)
            msg("You Crashed!!")
            pygame.mixer.music.stop()    


        
        def scoring(dodged,score,obSpeed,multiplier):
            font = pygame.font.SysFont(None,30)
            text = font.render("Cars Dodged "+str(dodged),True,black)
            scores = font.render("Score "+str(score),True,red)
            multiplier_count=font.render("Multiplier "+str(multiplier),True,black)
            life_count=font.render("Lives "+str(life),True,black)
            Acc_count=font.render("Nitrous "+str(accelerate),True,black)
            
            gameDisplay.blit(text,(10,50))
            gameDisplay.blit(scores,(10,20))
            gameDisplay.blit(multiplier_count,(10,80))
            gameDisplay.blit(life_count,(10,110))
            gameDisplay.blit(Acc_count,(10,140))

        def coin(coinStart_x,coinStart_y):
            gameDisplay.blit(coins,(coinStart_x,coinStart_y))

        def Life(LifeStart_x,LifeStart_y):
            gameDisplay.blit(life_pic,(LifeStart_x,LifeStart_y))

        def Acc(AccStart_x,AccStart_y):
            gameDisplay.blit(Acc_pic,(AccStart_x,AccStart_y))    

        def text_objects(text,font) :
            textSurface = font.render(text,True,black)
            return textSurface,textSurface.get_rect()
        def msg(text) :
            largetext = pygame.font.Font("freesansbold.ttf",115)
            TextSurf , TextRect = text_objects(text,largetext)
            TextRect.center = ((displayWidth / 2), (displayHeight / 2))
            gameDisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            time.sleep(2)
        def end () :
            msg("You Crashed")

            

              
            
        carWidth=64
        carHeight=128

        ob_width=64
        ob_height=128

        white=(255,255,255)
        black=(0,0,0)
        red = (255,0,0)

        #lead_x = displayWidth*0.45
        #lead_y = displayHeight*0.77
        lead_x_change = 0
        lead_y_change = 0

        #background = pygame.image.load('grass.jpg').convert()
        #background2 = pygame.image.load('road.jpg')
        #background = pygame.image.load('grass.jpg')
        def background():
            gameDisplay.blit(background,(0,0))
            
        carDistance = 444

        #Scores
        passed = 0
        score = 0
        level=0

        def userCar1Func():
            gameDisplay.blit(userCar1,(lead_x,lead_y))
        def userCar2Func():    
            gameDisplay.blit(userCar2,(lead_x,lead_y))

        

        def car(lead_x,lead_y):
            gameDisplay.blit(car_image,(lead_x,lead_y))


        def obstacle1(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob1.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle2(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob2.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle3(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob3.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle4(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob4.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle5(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob5.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))    
            

        carDistance=800-(ob_height+carHeight)    
        roadWidth = 423
        obRightCorner=obStart_x+64
        obLeftCorner=obStart_x
           
        gameExit = False
        while not gameExit:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        lead_x_change+=3
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        lead_x_change -=3
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        lead_y_change +=1
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        lead_y_change -=1
                    if accelerate!=0:
                        if event.key == pygame.K_SPACE:
                            obSpeed+=4.5
                        
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_d or event.key == pygame.K_a:
                    lead_x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    lead_y_change = 0
            if event.type == pygame.KEYUP:
                if accelerate!=0:
                    if event.key == pygame.K_SPACE:
                        obSpeed=9
                        accelerate-=1        
            if lead_x<125 or lead_x>(675-62):#car width = 62
                life=life-1
                if life==0:
                    end()
                    pygame.quit()


            if multiplier==0:
                if obStart_y>displayHeight:
                    obStart_y=0-ob_height
                    obStart_x=random.randrange(125,(675-64))
                    score+=10
                    dodged+=1
                    if dodged%10==0:
                        level+=1
                        obSpeed+=4.5
                        msg("Level "+str(level))
                        
            elif multiplier!=0:
                if obStart_y>displayHeight:
                    obStart_y=0-ob_height
                    obStart_x=random.randrange(125,(675-64))
                    score+=20
                    dodged+=1
                    multiplier-=1
                    if dodged%10==0:
                        level+=1
                        obSpeed+=4.5
                        msg("Level "+str(level))              
                
            

            if coinStart_y > displayHeight:
                coinStart_y = -15000
                coinStart_x = random.randrange(125,(675-56))

            if (coinStart_y+coinHeight)> lead_y:
                if lead_x > coinStart_x and lead_x < (coinStart_x + coinWidth) or (lead_x + carWidth) > coinStart_x and (lead_x + carWidth) < (coinStart_x + coinWidth):
                    coinStart_y=-6200 
                    multiplier+=1

            if (LifeStart_y+coinHeight)> lead_y:
                if lead_x > LifeStart_x and lead_x < (LifeStart_x + coinWidth) or (lead_x + carWidth) > LifeStart_x and (lead_x + carWidth) < (LifeStart_x + coinWidth):
                    LifeStart_y=-15000
                    life+=1       

            if LifeStart_y > displayHeight:
                LifeStart_y =-15000
                LifeStart_x = random.randrange(125,(675-56))

            if (AccStart_y+coinHeight)> lead_y:
                if lead_x > AccStart_x and lead_x < (AccStart_x + coinWidth) or (lead_x + carWidth) > AccStart_x and (lead_x + carWidth) < (AccStart_x + coinWidth):
                    AccStart_y=-15000
                    accelerate=1       

            if AccStart_y > displayHeight:
                AccStart_y =-15000
                AccStart_x = random.randrange(125,(675-56))
                
            
            if lead_x<125 or lead_x>(675-62):#car width = 62
                life=life-1
                lead_x = displayWidth*0.45
                lead_y = displayHeight*0.7
                if life==0:
                    crash(lead_x,lead_y)
                    
                    intro_loop()

            if (obStart_y+ob_height)> lead_y:
                if lead_x > obStart_x and lead_x < (obStart_x + ob_width) or (lead_x + carWidth) > obStart_x and (lead_x + carWidth) < (obStart_x + ob_width):
                    life=life-1
                    lead_x = displayWidth*0.45
                    lead_y = displayHeight*0.77
                    if life==0:
                        crash(lead_x,lead_y)
                        
                        intro_loop()

                     
            lead_x += lead_x_change
            lead_y += lead_y_change
            gameDisplay.fill(white)
          
            
            rel_y = y % background1.get_rect().width
            gameDisplay.blit(background1,(0,rel_y-background1.get_rect().width))
            y+=obSpeed
            if rel_y < 800:
                gameDisplay.blit(background1,(0,rel_y))
            
            obStart_y-=(obSpeed/4)
            
            obStart_y+=obSpeed

            ob = random.randrange(0,3)
            if dodged%3==0:
                obstacle1(obStart_x,obStart_y)
            elif dodged%3==1:
                obstacle2(obStart_x,obStart_y)
            elif dodged%3==2:
                obstacle3(obStart_x,obStart_y)
            elif dodged%2==0:
                obstacle4(obStart_x,obStart_y)

            coinStart_y-=(obSpeed/4)
            coin(coinStart_x,coinStart_y)
            coinStart_y+=obSpeed
            if coinStart_y == obStart_y+100 and coinStart_x == obStart_x + 50:
                coinStart_y = -7000

            LifeStart_y-=(obSpeed/4)
            Life(LifeStart_x,LifeStart_y)
            LifeStart_y+=obSpeed
            if LifeStart_y == obStart_y+100 and LifeStart_x == obStart_x + 50:
                LifeStart_y = -9000 
             
            AccStart_y-=(obSpeed/4)
            Acc(AccStart_x,AccStart_y)
            AccStart_y+=obSpeed
            
            
            #score_system(dodged,score,multiplier,life,jump)

            #firstCar = userCar1Func()
            #secondCar = userCar2Func()
            car(lead_x,lead_y)
            

            

            scoring(dodged,score,obSpeed,multiplier)
            #clock.tick(60)
            pygame.display.update()            
        pygame.quit()
        quit()
        game_loop()
        
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

def game_loop_HARD():
        pygame.mixer.music.load('music/coffee_stains.wav')
        pygame.mixer.music.play(-1)
        global LifeStart_x,LifeStart_y,AccStart_x,AccStart_y,accelerate,lead_x,lead_y
        pygame.init()
        displayWidth = 800
        displayHeight = 600

        gameDisplay = pygame.display.set_mode((displayWidth,displayHeight))
        gameDislpay = pygame.display.set_caption('The Crash')

        ditch_pic=pygame.image.load("ditch_2.png")
        ditch_x=random.randrange(125,(675-70))
        ditch_y=-10000
        
        #car_image = pygame.image.load('car1.png')
        #background = pygame.image.load('grass.jpg')
        coins = pygame.image.load('coin.png')



        coinHeight=56
        coinWidth=56


        jump=0
        life=1
        multiplier=0
        score=0
        dodged=0
        

        y=0

        obSpeed = 10
        obStart_y=-750
        obStart_x=random.randrange(125,(675-62))

        coinSpeed = 2
        coinStart_y=-1500
        coinStart_x=random.randrange(125,(675-56))
        
        def coin(coinStart_x,coinStart_y):
            gameDisplay.blit(coins,(coinStart_x,coinStart_y))

        def crash(lead_x,lead_y):
            car_crash = pygame.image.load('carcrash.png')
            gameDisplay.blit(car_crash, (obStart_x,obStart_y+100))
            crash_sound = pygame.mixer.Sound("music/crash.wav")
            pygame.mixer.Sound.play(crash_sound)
            msg("You Crashed!!")
            pygame.mixer.music.stop()    


        
        def scoring(dodged,score,obSpeed,multiplier):
            font = pygame.font.SysFont(None,30)
            text = font.render("Cars Dodged "+str(dodged),True,black)
            scores = font.render("Score "+str(score),True,red)
            multiplier_count=font.render("Multiplier "+str(multiplier),True,black)
            life_count=font.render("Lives "+str(life),True,black)
            Acc_count=font.render("Nitrous "+str(accelerate),True,black)
            
            gameDisplay.blit(text,(10,50))
            gameDisplay.blit(scores,(10,20))
            gameDisplay.blit(multiplier_count,(10,80))
            gameDisplay.blit(life_count,(10,110))
            gameDisplay.blit(Acc_count,(10,140))

        def coin(coinStart_x,coinStart_y):
            gameDisplay.blit(coins,(coinStart_x,coinStart_y))

        def Life(LifeStart_x,LifeStart_y):
            gameDisplay.blit(life_pic,(LifeStart_x,LifeStart_y))

        def Acc(AccStart_x,AccStart_y):
            gameDisplay.blit(Acc_pic,(AccStart_x,AccStart_y))
            
        def text_objects(text,font) :
            textSurface = font.render(text,True,black)
            return textSurface,textSurface.get_rect()
        def msg(text) :
            largetext = pygame.font.Font("freesansbold.ttf",115)
            TextSurf , TextRect = text_objects(text,largetext)
            TextRect.center = ((displayWidth / 2), (displayHeight / 2))
            gameDisplay.blit(TextSurf,TextRect)
            pygame.display.update()
            time.sleep(2)
        def end():
            msg("You Crashed")

            

              
            
        carWidth=64
        carHeight=128

        ob_width=64
        ob_height=128

        lead_x_change = 0
        lead_y_change = 0
        def background():
            gameDisplay.blit(background,(0,0))
            
        carDistance = 444

        #Scores
        passed = 0
        score = 0
        level=0

        def car(lead_x,lead_y):
            gameDisplay.blit(car_image,(lead_x,lead_y))


        def obstacle1(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob1.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle2(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob2.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle3(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob3.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle4(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob4.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))
        def obstacle5(obStart_x,obStart_y):
                ob_pic = pygame.image.load("ob5.png")    
                gameDisplay.blit(ob_pic,(obStart_x,obStart_y))    

        gameExit = False
        while not gameExit:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if ditch_y > lead_y:
                            lead_x_change-=3
                        else :
                            lead_x_change+=3
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if ditch_y > lead_y :
                            lead_x_change+=3
                        else :
                            lead_x_change-=3
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        lead_y_change +=1
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        lead_y_change -=1
                    if accelerate!=0:
                        if event.key == pygame.K_SPACE:
                            obSpeed+=4.5
                        
                        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or event.key == pygame.K_a or event.key == pygame.K_d:
                    lead_x_change = 0
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_w or event.key == pygame.K_s:
                    lead_y_change = 0
            if event.type == pygame.KEYUP:
                if accelerate!=0:
                    if event.key == pygame.K_SPACE:
                        obSpeed=10
                        accelerate-=1
                        
            if lead_x<125 or lead_x>(675-62):#car width = 62
                life=life-1
                if life==0:
                    end()
                    pygame.quit()

            if multiplier==0:
                if obStart_y>displayHeight:
                    obStart_y=0-ob_height
                    obStart_x=random.randrange(125,(675-64))
                    score+=10
                    dodged+=1
                    if dodged%10==0:
                        level+=1
                        obSpeed+=4.5
                        msg("Level "+str(level))
                        
            elif multiplier!=0:
                if obStart_y>displayHeight:
                    obStart_y=0-ob_height
                    obStart_x=random.randrange(125,(675-64))
                    score+=20
                    dodged+=1
                    multiplier-=1
                    if dodged%10==0:
                        level+=1
                        obSpeed+=4.5
                        msg("Level "+str(level))              
                
            

            if coinStart_y > displayHeight:
                coinStart_y = -15000
                coinStart_x = random.randrange(125,(675-56))

            if (coinStart_y+coinHeight)> lead_y:
                if lead_x > coinStart_x and lead_x < (coinStart_x + coinWidth) or (lead_x + carWidth) > coinStart_x and (lead_x + carWidth) < (coinStart_x + coinWidth):
                    coinStart_y=-6200 
                    multiplier+=1

            if (LifeStart_y+coinHeight)> lead_y:
                if lead_x > LifeStart_x and lead_x < (LifeStart_x + coinWidth) or (lead_x + carWidth) > LifeStart_x and (lead_x + carWidth) < (LifeStart_x + coinWidth):
                    LifeStart_y=-15000
                    life+=1       

            if LifeStart_y > displayHeight:
                LifeStart_y =-15000
                LifeStart_x = random.randrange(125,(675-56))

            if (AccStart_y+coinHeight)> lead_y:
                if lead_x > AccStart_x and lead_x < (AccStart_x + coinWidth) or (lead_x + carWidth) > AccStart_x and (lead_x + carWidth) < (AccStart_x + coinWidth):
                    AccStart_y=-15000
                    accelerate=1       

            if AccStart_y > displayHeight:
                AccStart_y =-15000
                AccStart_x = random.randrange(125,(675-56))
                
            
            if lead_x<125 or lead_x>(675-62):#car width = 62
                life=life-1
                lead_x = displayWidth*0.45
                lead_y = displayHeight*0.7
                if life==0:
                    crash(lead_x,lead_y)
                    
                    intro_loop()

            if (obStart_y+ob_height)> lead_y:
                if lead_x > obStart_x and lead_x < (obStart_x + ob_width) or (lead_x + carWidth) > obStart_x and (lead_x + carWidth) < (obStart_x + ob_width):
                    life=life-1
                    lead_x = displayWidth*0.45
                    lead_y = displayHeight*0.77
                    if life==0:
                        crash(lead_x,lead_y)
                        
                        intro_loop()

                     
            lead_x += lead_x_change
            lead_y += lead_y_change
            gameDisplay.fill(white)
          
            
            rel_y = y % background1.get_rect().width
            gameDisplay.blit(background1,(0,rel_y-background1.get_rect().width))
            y+=obSpeed/1.2
            if rel_y < 800:
                gameDisplay.blit(background1,(0,rel_y))
            
            obStart_y-=(obSpeed/4)
            
            obStart_y+=obSpeed

            ob = random.randrange(0,3)
            if dodged%3==0:
                obstacle1(obStart_x,obStart_y)
            elif dodged%3==1:
                obstacle2(obStart_x,obStart_y)
            elif dodged%3==2:
                obstacle3(obStart_x,obStart_y)
            elif dodged%2==0:
                obstacle4(obStart_x,obStart_y)

            coinStart_y-=(obSpeed/4)
            coin(coinStart_x,coinStart_y)
            coinStart_y+=obSpeed
            if coinStart_y == obStart_y+100 and coinStart_x == obStart_x + 50:
                coinStart_y = -7000

            LifeStart_y-=(obSpeed/4)
            Life(LifeStart_x,LifeStart_y)
            LifeStart_y+=obSpeed
            if LifeStart_y == obStart_y+100 and LifeStart_x == obStart_x + 50:
                LifeStart_y = -9000 
             
            AccStart_y-=(obSpeed/4)
            Acc(AccStart_x,AccStart_y)
            AccStart_y+=obSpeed
            
            
            #score_system(dodged,score,multiplier,life,jump)

            #firstCar = userCar1Func()
            #secondCar = userCar2Func()

            gameDisplay.blit(ditch_pic,(ditch_x,ditch_y))
            ditch_y=ditch_y + 6
            if ditch_y > lead_y + 400 :
                ditch_y = -10000
            
            car(lead_x,lead_y)
            

            

            scoring(dodged,score,obSpeed,multiplier)
            #clock.tick(60)
            pygame.display.update()            
        pygame.quit()
        quit()
        game_loop()        
        
pygame.display.update()        
intro_loop()
pygame.quit()
quit()                
