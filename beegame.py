import pgzrun
from random import randint 

WIDTH = 600
HEIGHT = 600

score = 0
gameover = False

bee = Actor("beesprite")
bee.pos = (104,105)

flower = Actor("flowersprite")
flower.pos = (204,205)

def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("Score " + str(score),color = "black" , topleft =(10,10))

    if gameover:
        screen.fill("pink")
        screen.draw.text("Your time is up, your final score is: "+ str(score),midtop =(WIDTH/2,10),fontsize = 40,color = "blue")


def place_flower():
    flower.x = randint(70,(WIDTH-70))
    flower.y = randint(70,(HEIGHT-70))

def times_up():
    global gameover
    gameover = True

def update():
    global score
    if keyboard.left:
       bee.x = bee.x - 2
    if keyboard.right:
       bee.x = bee.x + 2
    if keyboard.up:
     bee.y = bee.y - 2
    if keyboard.down:
     bee.y = bee.y + 2 
 
    flower_collected = bee.colliderect(flower)
    if flower_collected:
       score = score + 10
       place_flower()

clock.schedule(times_up,60.0)

pgzrun.go()


