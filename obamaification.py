from Myro import *
PICTURE=makePicture("future_50.jpg")
getPixels("future_50.jpg")=Pixels
print(Pixel)
#show(getPixels(Picture))
#def PIXEL=
#getRed(PIXEL)
ObamaDarkBlue = makeColor(0,51,76)
ObamaRed = makeColor(217, 26, 33)
ObamaBlue = makeColor(112,150,158)
ObamaYellow = makeColor(252, 227, 166)
for i in Pixels:
    if getGray(i)>180:
        setColor(i,ObamaYellow)
    elif getGray (i)>120:
        setColor(i,ObamaBlue) 
    elif getGray (i)>60:
        setColor (i, ObamaRed)
    else:
        (i, ObamaDarkBlue)
     


