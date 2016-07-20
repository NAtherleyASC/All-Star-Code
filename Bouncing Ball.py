from Processing import*
from random import *

#Bouncing Ball

#setup: creating the ball,the window, four walls
#make ball move in random direction (randrange()) change position of the image so it looks like it's moving
#conditionals for when balls hit the wall(if the cordinatinate of the ball and the wall are in the same place reverse direction)
#make it so when the ball hits the wall it bounces in an upward or downward direction fronm the wall

width= 460
height= 460
xPos =randrange(50,450)
yPos=randrange(150, 350)
xPos2= randrange(25, 250)
yPos2= randrange(35, 125)
moveByX=randrange(15)
moveByY=randrange(15)
moveByX2=randrange(15)
moveByY2=randrange(15)
def setup():
    
    window(500, 500)
    #background(255, 255, 0)
    #strokeWeight(5)
    #fill(0,255,0)
    #rect(20, 20, width, height)
    #fill(0,0,0)
    ellipse(xPos, yPos, 50, 50)
    
   
 
setup()

#def stop():
    

def move():
    global xPos,yPos,moveByX,moveByY, xPos2,yPos2,moveByX2,moveByY2
    while xPos<500 and yPos<500 and xPos>0 and yPos>0 and xPos2<500 and yPos2<500 and xPos2>0 and yPos2>0 :
        background(192, 192, 192,10)
        #fill(0,225, 0)
        #rect(20, 20, width, height)
        xPos=xPos+moveByX
        yPos=yPos+moveByY
        xPos2=xPos2+moveByX2
        yPos2=yPos2+moveByY2
        #fill(0, 0, 225)
        ellipse(xPos, yPos, 50, 50)
        ellipse(xPos2, yPos2, 50, 50)
        delay(25)
        if xPos>450 or xPos<50:
            fill(randrange(255),randrange(255),randrange(255))
            moveByX=-moveByX
        if yPos<50 or yPos>450:
            fill(randrange(255),randrange(255),randrange(255))
            moveByY=-moveByY
        if xPos2>450 or xPos2<50:
            fill(randrange(255),randrange(255),randrange(255))
            moveByX2=-moveByX2
        if yPos2<50 or yPos2>450:
            fill(randrange(255),randrange(255),randrange(255))
            moveByY2=-moveByY2
       
 


        

while True:        
    move()
    #move3()
    #move4()
            
            
    #else:   
        #xPos==460
    
  

    #background(255, 255, 0)
    

#move()
    #ellipse (mouseX-5, mouseY-5, 50, 50)
       
        
    
    
    
#draw()


    
    
