#Pedro Gallino
#10/5/17
#dotDemo.py - making some dots

from ggame import *

red = Color(0xff0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for i in range(20):
    Sprite(dot,(20+50*i,20))

App().run()
