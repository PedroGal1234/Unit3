#Pedro Gallino
#10/5/17
#dotDemo.py - making some dots

from ggame import *

red = Color(0xff0000,1)

dot = CircleAsset(20,LineStyle(1,red),red)

for j in range(26): #pritns that row times
    for i in range(50):#prints one row of dots
        Sprite(dot,(20+20*i,20+20*j))

App().run()
