from Processing import *
from random import *

#Space Invaders


#setup:
    #window
    #background
    #spaceship
    #row of UFOs
    #barriers (bonus)
    
#function for the UFOs:
    #list and for the loop
    #increment so UFOs can move
    #shoots ellipses bullet size
    
#function for bullets:

    #bullets don't move on the x axis (just go straight up)
    #have bullets not moving with the spaceship
    #mouseclicked
    
window(500,500)
moveByX=randrange(15)
moveByY=randrange(15)
moveByX2=randrange(15)
moveByY2=randrange(15)

xPos2= 60
yPos2= 20

yPos= 20


width= 30

x=250
y=420
xChange=0

def draw():
    background(0,0,0)
    fill(255, 255, 255)
    rect(150, 20, 30, 30)
    rect(200, 20, 30, 30)
    rect(250, 20, 30, 30)
    rect(300, 20, 30, 30)
    rect(350, 20, 30, 30)
    fill(82,236,4)
    rect(x,420,50,50)
    fill(255,255,255)
    ellipse(x,y,20,20)


       
        
    

def setup():
    #global yPos,#xPos2, yPos2, moveByX, moveByY,moveByX2, moveByY2
    background(0,0,0)
    fill(255, 255, 255)
    rect(150, 20, 30, 30)
    rect(200, 20, 30, 30)
    rect(250, 20, 30, 30)
    rect(300, 20, 30, 30)
    rect(350, 20, 30, 30)
    rectXList= [150, 200, 250, 300, 350]
    rectY= 20
    y= 420
    
    
    
    #background(0,0,0)
    #ufos= [i, i, i, i, i]
    #print(ufos)
    
    #width= 30
    #height= 30
      
      
      
    ''' 
    i=0
    while i<5:
        newX=(width*i)
        i=i+1
        rect(newX+180, 20,30, 30)
        #rect(newX+40, 0,30, 30)
        #rect(newX+60, 0,30, 30)
        xPos= newX+180
    
 
    
        while xPos<500 and yPos<500 and xPos>0 and yPos>0:
            background(0,0,0)
            xPos=xPos+moveByX
            yPos=yPos+moveByY
            fill(255, 255, 255)
            rect(xPos, yPos, 30, 30)
            rect(xPos2, yPos2, 30, 30)
            #rect(xPos, yPos, 30, 30)
            #rect(xPos, yPos, 30, 30)
            #rect(xPos, yPos, 30, 30)
            delay(100)
            
            if xPos>450 or xPos<50:
                #fill(randrange(255),randrange(255),randrange(255))
                moveByX=-moveByX
            if yPos<50 or yPos>450:
               # fill(randrange(255),randrange(255),randrange(255))
                moveByY=-moveByY
            if xPos2>450 or xPos2<50:
                #fill(randrange(255),randrange(255),randrange(255))
                moveByX2=-moveByX2
            if yPos2<50 or yPos2>450:
               # fill(randrange(255),randrange(255),randrange(255))
                moveByY2=-moveByY2
'''
    
setup()

def shoot(): 
    global y
    rectY= 20
    rectXList= [150, 200, 250, 300, 350]
    background(0,0,0)
    fill(255, 255, 255)
    rect(150, 20, 30, 30)
    rect(200, 20, 30, 30)
    rect(250, 20, 30, 30)
    rect(300, 20, 30, 30)
    fill(255,255,255)
    ellipse(x,y,20,20)
    y=y-20
    delay(20)
    for rectX in rectXList:
        if rectX<=x<=rectX+width and y== rectY:
           background( 0, 0, 0)
           rectXList.remove(rectX)
           return rectList
shoot()

def doKeyPressed():
    global x,y
    rectY= 20
    rectXList= [150, 200, 250, 300, 350]
    background(0,0,0)
    fill(255, 255, 255)
    rect(150, 20, 30, 30)
    rect(200, 20, 30, 30)
    rect(250, 20, 30, 30)
    rect(300, 20, 30, 30
    if key()== "a":
         x=x-10
    if key() == "d":
        x=x+10
    elif key() == "space":
            y=y-20
            shoot()
    draw()
onKeyPressed+=doKeyPressed
print(key)
doKeyPressed()


#color and shape of spaceship

    

#function to make the spaceship move



    