import pgzrun

#screen dimensions
WIDTH = 1000
HEIGHT = 1000

ship = Actor('ship')

ship.pos = (WIDTH/10, HEIGHT-60)

if keyboard.left:
    ship.x = ship.x - 10

elif keyboard.right:
    ship.x = ship.x + 10

elif keyboard.up:
    ship.y = ship.y + 10

elif keyboard.down:
    ship.y = ship.y - 10      

def draw():
    screen.draw.filled_circle((300,400),50,"Blue") 
    box = Rect((100,200),(80,80))
    box2 = Rect((200,340),(63,80))
    box4 = Rect((596,240),(100,100))
    screen.draw.rect(box,"Cyan")
    screen.draw.filled_rect(box4,"Silver")
    screen.draw.filled_rect(box2, "Gold")
    ship.draw()

def update():

 if keyboard.left:
    ship.x = ship.x - 10

 elif keyboard.right:
    ship.x = ship.x + 10

 elif keyboard.up:
    ship.y = ship.y - 10

 elif keyboard.down:
    ship.y = ship.y + 10    


pgzrun.go()