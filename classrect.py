import pygame,sys
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Hello Pygame")
#Colors
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow = (255,255,0)
#Screen Fill
screen.fill("White")
pygame.display.update()
while True:
    #Creating a rectangle class
    class Rect():
        def __init__(self,color,dimensions):
            self.rect_surf = screen
            self.rect_color = color
            self.rect__dimensions = dimensions

        def draw(self):
            self.Draw_Rect = pygame.draw.rect(self.rect_surf, self.rect_color, self.rect__dimensions)

    #creating Instances

    greenRect = Rect(green,(50,20,100,100))
    redRect=Rect(red,(150,200,150,150))
    blueRect = Rect(blue,(300,400,200,200))
    yellowRect = Rect(yellow,(125,255,125,125))
    #accessingmethods
    greenRect.draw()
    redRect.draw()
    blueRect.draw()
    yellowRect.draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    class Circle():
        def __init__(self,color,position,Diameter):
            self.circle_surf = screen
            self.circle_color = color
            self.circle_position = position
            self.circle_diameter = Diameter

        def draw(self):
            self.Draw_Circle = pygame.draw.circle(self.circle_surf, self.circle_color, self.circle_position, self.circle_diameter)
        
        #creating Instances

    greenCircle = Circle(green,(430,406),(120))
    redCircle = Circle(red,(561,111),(64))
    blueCircle = Circle(blue,(488,91),(100))
    yellowCircle = Circle(yellow,(275,104),(150))
    #accessingmethods
    greenCircle.draw()
    redCircle.draw()
    blueCircle.draw()
    yellowCircle.draw()
        
    pygame.display.update()