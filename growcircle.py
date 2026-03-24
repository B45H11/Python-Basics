import pygame
pygame.init()
#global variables
screen = pygame.display.set_mode([1000,1000])
red = (0,255,0)
blue = (255,0,0)
green = (10,13,0)
pink = (255,0,255)
yellow = (255,255,0)
black = (0,0,0)
white=(255,255,255)

screen.fill(white)

class myCircle():
    def __init__(self,color, pos, rad, wid=0):
        self.color = color
        self.pos = pos
        self.rad = rad
        self.wid = wid
        self.scrn = screen

    def draw(self):
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

    def grow(self,x):
        self.rad += x
        pygame.draw.circle(self.scrn, self.color, self.pos, self.rad, self.wid)

#how to draw a circle
position = (500,500)
radius = 50
wid = 2
pygame.draw.circle(screen, radius, position, wid)
pygame.display.update()

#creating instances
pinkCircle = myCircle(pink, position, radius+60)
yellowCircle = myCircle(yellow, position, radius+0)
redCircle = myCircle(red, position, radius, 5)
blueCircle = myCircle(blue, position, 20)



while(1):
    for event in pygame.event.get():
        if (event.type == pygame.MOUSEBUTTONDOWN):
            pinkCircle.draw()
            yellowCircle.draw()
        elif (event.type == pygame.MOUSEBUTTONUP):
            pinkCircle.grow(10)
            yellowCircle.grow(5)
        elif (event.type == pygame.MOUSEMOTION):
            pos = pygame.mouse.get_pos()
            blackCircle = myCircle(black, pos, 5)
            blackCircle.draw()
            pygame.display.update()

        elif event.type == pygame.QUIT:
            pygame.quit()