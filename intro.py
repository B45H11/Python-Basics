print("Sebastian")

import pgzrun

def draw():
    screen.draw.line((100,100),(300,300),("Pink"))
    screen.draw.circle((300,300),50,"Yellow") 
    screen.draw.filled_circle((300,400),50,"Blue") 
    box = Rect((100,200),(80,80))
    box1 = Rect((150,300),(90,180))
    box2 = Rect((0,37),(100,300))
    box3 = Rect((300,350),(200,35))
    box4 = Rect((596,240),(100,100))
    box5 = Rect((405,200),(50,150))
    box6 = Rect((204,100),(68,87))
    box7 = Rect((500,150),(100,74))
    screen.draw.rect(box,"Cyan")
    screen.draw.rect(box1,"White")
    screen.draw.rect(box2,"Red")
    screen.draw.rect(box3,"Green")
    screen.draw.rect(box4,"Silver")
    screen.draw.rect(box5,"Maroon")
    screen.draw.rect(box6,"Orange")
    screen.draw.rect(box7,"Gold")

pgzrun.go()