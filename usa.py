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

Horizontal = 0
for i in range(1,51):
    if i<=6:
        star = PolygonAsset([(0,5.5),(5,5),(6.5,0),(9,5),(14,5.5),(10.5,9),(12,14),(6.5,11.5),(2,14),(3.5,9)],whiteOutline,white)
        Sprite(star,(110+Horizontal,40))
        Horizontal = Horizontal + 49





App().run()
    
