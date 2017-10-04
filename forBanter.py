#Pedro Gallino
#10/2/17
#forBanter.py - Fooling Around


red = Color(0xff0000,1)
green = Color(0x00ff00,1)
blue = Color(0x000ff,1)
black = Color(0x00000,1)

redOutline = LineStyle(2,red)
greenOutline = LineStyle(2,black)
blueOutline = LineStyle(2,blue)
blackOutline = LineStyle(2,black)

redRectangle = RectangleAsset(100,100,blackOutline,red)
Sprite(redRectangle,(175,100))

move = input('Move with w, a, s, d,')
vertical = 400
horizontal = 400

while True:
    if move == 'w': 
        vertical = +100
        Sprite(redRectangle,(vertical,horizontal))
    if move == 'lol':
        break


App().run()





