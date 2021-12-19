import pygame
import random

"""
Assets
"""
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY1 = (100,100,100)
image = pygame.image.load(r'images/tree2.png')
image = pygame.transform.scale(image, (750,1000))    # 4: 5 scale
treebase = pygame.image.load(r'images/coffee-bottom.png')
treebase = pygame.transform.scale(treebase, (100,140))
treebase = pygame.transform.rotate(treebase, 180)
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

leaf = pygame.image.load('images/leaf.png')
leaf = pygame.transform.scale(leaf, (40,60)) # 2:3

leaves = [
    pygame.transform.rotate(leaf, -10),
    pygame.transform.rotate(leaf, -5),
    pygame.transform.rotate(leaf, 0),
    pygame.transform.rotate(leaf, 5),
    pygame.transform.rotate(leaf, 10),
]


font1 = pygame.font.Font('fonts/notosanskr.ttf', 70) 

text1 = font1.render("텀블러 쓰세요", True, WHITE)


#screen = pygame.display.set_mode([1600, 1200], pygame.FULLSCREEN) 
screen = pygame.display.set_mode([1920, 1200], pygame.RESIZABLE) # use only by 1600

clock = pygame.time.Clock()

target_cnt = 50
current_cnt = 10 # TODO change this
ratio = current_cnt / target_cnt
# make 5 interim steps

def getXRange(r):
    return (100 + 375*r, 850-370*r)
def getY(r):
    return 950 - 750*r

numLeaves = 200



"""
Tree
"""
riseinterval = 10
def drawTree():
    # screen.blit(image, (200, 675 - current_cnt*riseinterval)) # center: 400
    # draw star
    screen.blit( stars[0], (425, 200) )

    screen.blit(image, ( 100, 200))
    screen.blit(treebase, (420,1080))

"""
Cups
"""
def drawCups():
    
    screen.blit(leaves[0], (400,800))

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
    # x1 = 100
    # x2 = 700
    # pygame.draw.line(screen, GRAY1, [x1,675 - 10*riseinterval], [x2,675 - 10*riseinterval], 5)
    # pygame.draw.line(screen, GRAY1, [x1,675 - 20*riseinterval], [x2,675 - 20*riseinterval], 5)
    # pygame.draw.line(screen, GRAY1, [x1,675 - 30*riseinterval], [x2,675 - 30*riseinterval], 5)
    # pygame.draw.line(screen, GRAY1, [x1,675 - 40*riseinterval], [x2,675 - 40*riseinterval], 5)
    # pygame.draw.line(screen, GRAY1, [x1,675 - 50*riseinterval], [x2,675 - 50*riseinterval], 5)

    screen.blit(text1, [1200, 500])

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
    drawDesc()
    #drawBottom()
    drawTree()
    drawCups()
    drawSnow()
    

	# make clock tick 
    clock.tick(60)

	# show surface
    pygame.display.flip()

pygame.quit()

#pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)