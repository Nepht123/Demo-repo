import pygame as pg
pg.init()
#pygame.init() allows us to initialize and begin to use pygame features


#Here I am creating the game screen
screen=pg.display.set_mode((800,600))#Here I am determining the size of my screen
'''Now this did succesfully creat the screen but the issue is that the screen will show as long as the programe is running,
   but the programe only takes a few seconds to finish running.
   So I need to find a way to keep it running,
   while still having a way to shut it down when neccesary in order to close the game
'''

#To fix this running issue we are going to use something called events
'''An event is anything that is happening inside a game window but we will get more into it a bit later'''

running =True

#Changing the Title and Icon of window 
pg.display.set_caption("Alien terrorists")

#   This is where I will store the Image


icon=pg.image.load('C:\\Users\\mwamb\\OneDrive\\Desktop\\Git  Desktop demo\\Demo-repo\\github_py_projects\\Game_in_python\\Alien terorist.png')
pg.display.set_icon(icon)


print("Hello")
#This is the game loop, this loop will ensure that the program continues rubbibg until the window is closed 
while running:
    for events in pg.event.get():#This will go through every single possible event in the pygame library 
        if events.type == pg.QUIT:#If the event that as happened is to close the game window, this programe will stop running 
            running=False

