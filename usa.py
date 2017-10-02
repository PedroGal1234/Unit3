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

PolygonAsset([(0,0),(120,180),(60,300)],blackOutline,red)

App().run()
    
