#Pedro Gallino
#10/2/17
#warmUp10.py - makes wall paper

from ggame import *

red = Color(0xff0000,1)
white = Color(0xffffff,1)
blue = Color(0x00099,1)

redOutline = LineStyle(1,red)
whiteOutline = LineStyle(1,white)
blueOutline = LineStyle(.001,blue)

hs = 162.25
vs =81.25 

for k in range(25):
    for j in range(25):
        down = 0
        for shortLines in range(1,9):
            if shortLines%2 == 0:
                outline = whiteOutline = LineStyle(1,white)
                color = white
            else:
                outline = redOutline = LineStyle(1,red)
                color = red
            shortRectangle = RectangleAsset(87.5,6.25,outline,color)
            down = down+6.25
            Sprite(shortRectangle,(100+j*hs,down+k*vs))

down = 50
for k in range(25):
    for j in range(25):
        for longLines in range (1,8):
            if longLines%2 == 0:
                outline = whiteOutline = LineStyle(1,white)
                color = white
            else:
                outline = redOutline = LineStyle(1,red)
                color = red
            shortRectangle = RectangleAsset(162.5,6.25,outline,color)
            down = down+6.25
            Sprite(shortRectangle,(25+j*hs,down+k*vs))

for k in range(25):
    for j in range(25):
        blueRectangle = RectangleAsset(75,43.75,blueOutline,blue)
        Sprite(blueRectangle,(25+j*hs,6.25+k*vs))

star = PolygonAsset([(0,1.375),(1.25,1.25),(1.625,0),(2.25,1.25),(3.5,1.375),(2.625,2.25),(3,3.5),(1.625,2.875),(.5,3.5),(.875,2.25)],whiteOutline,white)
for k in range(25):
    for j in range(25):
        for j in range(0,5):
            for i in range(0,6):
                Sprite(star,(27.5+13.25*i+j*hs,7+9*j+k*vs))
        for j in range(0,4):
            for i in range(0,5):
                Sprite(star,(33.75+13.25*i+j*hs,11.5+9*j+k*vs))

App().run()
    
