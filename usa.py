#Pedro Gallino
#10/2/17
#usa.py - prints US flag with loops

from ggame import *

red = Color(0xff0000,1)
white = Color(0xffffff,1)
blue = Color(0x00099,1)

redOutline = LineStyle(1,red)
whiteOutline = LineStyle(1,white)
blueOutline = LineStyle(.001,blue)

down = 0
for shortLines in range(1,9):
    if shortLines%2 == 0:
        outline = whiteOutline = LineStyle(1,white)
        color = white
    else:
        outline = redOutline = LineStyle(1,red)
        color = red
    shortRectangle = RectangleAsset(350,25,outline,color)
    down = down+25
    Sprite(shortRectangle,(400,down))

down = 200
for longLines in range (1,8):
    if longLines%2 == 0:
        outline = whiteOutline = LineStyle(1,white)
        color = white
    else:
        outline = redOutline = LineStyle(1,red)
        color = red
    shortRectangle = RectangleAsset(650,25,outline,color)
    down = down+25
    Sprite(shortRectangle,(100,down))

blueRectangle = RectangleAsset(300,175,blueOutline,blue)
Sprite(blueRectangle,(100,25))

horizontalRow1 = 0
horizontalRow2 = 0
horizontalRow3 = 0
horizontalRow4 = 0
horizontalRow5 = 0
horizontalRow6 = 0
horizontalRow7 = 0
horizontalRow8 = 0
horizontalRow9 = 0
for i in range(1,51):
    star = PolygonAsset([(0,5.5),(5,5),(6.5,0),(9,5),(14,5.5),(10.5,9),(12,14),(6.5,11.5),(2,14),(3.5,9)],whiteOutline,white)
    if i <= 6:
        Sprite(star,(110+horizontalRow1,28))
        horizontalRow1 = horizontalRow1 + 53
    elif i <= 11:
        Sprite(star,(135+horizontalRow2,46))
        horizontalRow2 = horizontalRow2 + 53
    elif i <= 17:
        Sprite(star,(110+horizontalRow3,64))
        horizontalRow3 = horizontalRow3 + 53
    elif i <= 22:
        Sprite(star,(135+horizontalRow4,82))
        horizontalRow4 = horizontalRow4 + 53
    elif i <= 28:
        Sprite(star,(110+horizontalRow5,100))
        horizontalRow5 = horizontalRow5 + 53
    elif i <= 33:
        Sprite(star,(135+horizontalRow6,118))
        horizontalRow6 = horizontalRow6 + 53
    elif i <= 39:
        Sprite(star,(110+horizontalRow7,136))
        horizontalRow7 = horizontalRow7 + 53
    elif i <= 44:
        Sprite(star,(135+horizontalRow8,154))
        horizontalRow8 = horizontalRow8 + 53
    elif i <= 60:
        Sprite(star,(110+horizontalRow9,172))
        horizontalRow9 = horizontalRow9 + 53

App().run()
    
