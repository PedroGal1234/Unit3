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

down = 0
for j in range(20):
    for k in range (25):
        for shortLines in range(1,9):
            if shortLines%2 == 0:
                outline = whiteOutline = LineStyle(1,white)
                color = white
            else:
                outline = redOutline = LineStyle(1,red)
                color = red
            shortRectangle = RectangleAsset(35,2.5,outline,color)
            down = down+2.5
            Sprite(shortRectangle,(40+50*k,down+j*30))
down = 20
for j in range(20): 
    for k in range(25):
        for longLines in range (1,8):
            if longLines%2 == 0:
                outline = whiteOutline = LineStyle(1,white)
                color = white
            else:
                outline = redOutline = LineStyle(1,red)
                color = red
                shortRectangle = RectangleAsset(65,2.5,outline,color)
                down = down+2.5
            Sprite(shortRectangle,(10,down))

for j in range(20): 
    for k in range(25):
        blueRectangle = RectangleAsset(30+50*k,17.5+j*30,blueOutline,blue)
        Sprite(blueRectangle,(10,2.5))

star = PolygonAsset([(0,5.5),(5,5),(6.5,0),(9,5),(14,5.5),(10.5,9),(12,14),(6.5,11.5),(2,14),(3.5,9)],whiteOutline,white)
for m in range(20):
    for n in range(25):
        for j in range(0,5):
            for i in range(0,6):
                Sprite(star,(110+53*i+n*50,28+36*j+m*30))
        for j in range(0,4):
            for i in range(0,5):
                Sprite(star,(135+53*i+n*50,46+36*j+m*30))

App().run()
    


