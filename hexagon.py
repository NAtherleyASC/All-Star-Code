from Myro import *
init("sim")
z=0
while z < 5:
    z=z+1
    i=0
    while i < 6:
        i=i+1
        penDown()
        forward(1,2)
        turnBy(60)