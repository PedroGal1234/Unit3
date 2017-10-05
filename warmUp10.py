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
for shortLines in range(1,9):
    if shortLines%2 == 0:
        outline = whiteOutline = LineStyle(1,white)
        color = white
    else:
        outline = redOutline = LineStyle(1,red)
        color = red
    shortRectangle = RectangleAsset(35,2.5,outline,color)
    down = down+2.5
    Sprite(shortRectangle,(40,down))

for j in range(20): 
    for k in range(25):
    down = 20
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

horizontalRow1 = 0
horizontalRow2 = 0
horizontalRow3 = 0
horizontalRow4 = 0
horizontalRow5 = 0
horizontalRow6 = 0
horizontalRow7 = 0
horizontalRow8 = 0
horizontalRow9 = 0
star = PolygonAsset([(0,.55),(.5,.5),(.65,0),(.9,.5),(1.4,.55),(1.05,.9),(1.2,1.4),(.65,1.15),(.2,1.4),(.35,.9)],whiteOutline,white)

for j in range(20): 
    for k in range(25):
        for i in range(1,51):
            if i <= 6:
                Sprite(star,(110+horizontalRow1+50*k,2.8+j*30))
                horizontalRow1 = horizontalRow1 + 5.3
            elif i <= 11:
                Sprite(star,(135+horizontalRow2+50*k,4.6+j*30))
                horizontalRow2 = horizontalRow2 + 5.3
            elif i <= 17:
                Sprite(star,(110+horizontalRow3+50*k,6.4+j*30))
                horizontalRow3 = horizontalRow3 + 5.3
            elif i <= 22:
                Sprite(star,(135+horizontalRow4+50*k,8.2+j*30))
                horizontalRow4 = horizontalRow4 + 5.3
            elif i <= 28:
                Sprite(star,(110+horizontalRow5+50*k,10+j*30))
                horizontalRow5 = horizontalRow5 + 5.3
            elif i <= 33:
                Sprite(star,(135+horizontalRow6+50*k,11.8+j*30))
                horizontalRow6 = horizontalRow6 + 5.3
            elif i <= 39:
                Sprite(star,(110+horizontalRow7+50*k,13.6+j*30))
                horizontalRow7 = horizontalRow7 + 5.3
            elif i <= 44:
                Sprite(star,(135+horizontalRow8+50*k,15.4+j*30))
                horizontalRow8 = horizontalRow8 + 5.3
            elif i <= 60:
                Sprite(star,(110+horizontalRow9+50*k,17.2+j*30))
                horizontalRow9 = horizontalRow9 + 5.3

App().run()
    


