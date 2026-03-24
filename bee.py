import pgzrun
from random import randint
TITLE = "Catch the flower"

WIDTH = 800
HEIGHT = 500

bee = Actor('bee')
bee.pos = 0,100

flower = Actor('flower')
flower.pos = 45,125


score = 0
game_over = False
def draw():
    screen.blit("grass", (0,0))
    flower.draw()
    bee.draw()
    screen.draw.text("Score:" + str(score), color="white", topleft=(10,10))

    if game_over:
            screen.fill("black")
            screen.draw.text("Time's Up! Your score: " + str(score), midtop=(WIDTH/2,10),
            fontsize=50, color="white")


def place_flower():
        flower.x = randint(70, (WIDTH-70))
        flower.y = randint(70, (HEIGHT-70))
    

def time_up():
        global game_over
        game_over = True

def update():
     global score

     if keyboard.left:
         bee.x = bee.x - 5
     if keyboard.right:
         bee.x = bee.x + 5
     if keyboard.up:
         bee.y = bee.y - 5
     if keyboard.down:
         bee.y = bee.y + 5

     flower_collected = bee.colliderect(flower)

     if flower_collected:
         score = score + 10
         place_flower()
clock.schedule(time_up, 120.0)

pgzrun.go()

