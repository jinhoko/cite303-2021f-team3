import pygame
import random

"""
Assets
"""
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
image = pygame.image.load(r'images/tree1.png')
image = pygame.transform.scale(image, (400,500))    # 4: 5 scale
cupbase = pygame.image.load(r'images/coffee-bottom.png')
cupbase = pygame.transform.scale(cupbase, (50,100))
cupmiddle = pygame.image.load(r'images/coffee-stack.png')
cupmiddle = pygame.transform.scale(cupmiddle, (50,100))
starsize = (100,100)
stars = [ 
    pygame.transform.scale( pygame.image.load(r'images/s1.png'), starsize),
    pygame.transform.scale( pygame.image.load(r'images/s2.png'), starsize),
    pygame.transform.scale( pygame.image.load(r'images/s3.png'), starsize),
    pygame.transform.scale( pygame.image.load(r'images/s4.png'), starsize),
    pygame.transform.scale( pygame.image.load(r'images/s5.png'), starsize)
]

#screen = pygame.display.set_mode([1600, 1200], pygame.FULLSCREEN) 
screen = pygame.display.set_mode([1920, 1200], pygame.RESIZABLE) # use only by 1600

clock = pygame.time.Clock()

target_cnt = 50
current_cnt = 50 # TODO change this
# make 5 interim steps

def getProgress():
    if current_cnt < 10:
        return 1
    elif current_cnt < 20:
        return 2
    elif current_cnt < 30:
        return 3
    elif current_cnt < 40:
        return 4
    else:
        return 5

"""
Tree
"""
riseinterval = 10
def drawTree():
    screen.blit(image, (200, 675 - current_cnt*riseinterval)) # center: 400
    # draw star
    screen.blit( stars[getProgress() - 1], (400-50, 675 - current_cnt*riseinterval - 50) )

"""
Cups
"""
def drawCups():
    # draw first cup
    screen.blit(cupbase, (400-25, 1100))
    # draw others
    for i in range(current_cnt):
        screen.blit(cupmiddle, (400-25, 1100 - (i+1)*riseinterval ))

"""
Snow
"""
snowflakes = []
numSnow = 100
snowX1 = 0
snowX2 = 1600
snowY1 = 0
snowY2 = 1200
randSpeed = [2,3]
slowdown = 2    # 2, 3..
for q in range(numSnow):
    x = random.randrange(snowX1,snowX2)
    y = random.randrange(snowY1,snowY2)
    snowflakes.append([x,y,random.choice(randSpeed), 0])
def drawSnow():
    for i in snowflakes:
        i[3] +=1 
        if i[3] % slowdown == 0:
            i[1] += i[2]
            i[3] = 0
        pygame.draw.circle(screen, WHITE, i[:2], 4)
        
        if i[1] > snowY2:
            i[0] = random.randrange(snowX1, snowX2) 
            i[1] = random.randrange(-50 + snowY1, -5 + snowY1)

"""
Bottom
"""
# TODO set bottom
def drawBottom():
    pass

"""
Text / desc
"""
def drawDesc():
    pass


"""
Main Logic
"""

running = True
while running:

	# handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # check count updates

	# update elements
    screen.fill((0, 0, 0))

	# draw surface
    drawBottom()
    drawCups()
    drawTree()
    drawSnow()

	# make clock tick 
    clock.tick(60)

	# show surface
    pygame.display.flip()

pygame.quit()

#pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)