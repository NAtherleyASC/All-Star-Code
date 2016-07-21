from Processing import *
from random import *

#Battleship Project


#grid (would make into 2d list)
    #one for column 
    #one for row
#placing the ship
#when ships is hit or not (conditionals) 

gameOver = False
img = loadImage("explosiongif.gif")


def setup():
    global gameOver
    window(400, 400)
    board= [[0,0,0,0,0] ,[0,0,0,0,0]  ,[0,0,0,0,0] ,[0,0,0,0,0] ,[0,0,0,0,0]]
    row= randrange(0,5)
    column= randrange(0,5)
    board[row][column]= 1
    width= 80
    height= 80

    i=0
    while i<5:
        newX=width*i
        i=i+1
        line(newX, 0,newX, 400)
    i=0
    while i<5:
        newY=height*i
        i=i+1
        line(0, newY, 400, newY)
     
    
    while gameOver== False:   
        column= int(input ("which column?"))
        row= int(input ("which row?"))          
        if (board[row][column]==1)==False:
            print("missed ship")
            fill(255,0, 0)
            rect(width*row, height*column, 80,80)
        else:
            gameOver=True
            fill(0, 255, 0)
            image(img, 200, 200)
            #rect(width*row, height*column, 80,80)
            print("ship hit  won game")
            
        
    
setup()


