import pygame
import random

"""
Assets
"""
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
YELLOW= (255,233,0)
GRAY1 = (100,100,100)
GRAY2 = (200,200,200)

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
starback = pygame.image.load('images/star-back.png')
starback = pygame.transform.scale(starback, (400,400))

leaf = pygame.image.load('images/leaf.png')
leaf = pygame.transform.scale(leaf, (40,60)) # 2:3

leafImages = [
    # pygame.transform.rotate(leaf, -15),
    pygame.transform.rotate(leaf, -10),
    pygame.transform.rotate(leaf, -5),
    pygame.transform.rotate(leaf, 0),
    pygame.transform.rotate(leaf, 5),
    pygame.transform.rotate(leaf, 10),
    # pygame.transform.rotate(leaf, 15),
]

ornsize = (50,50)
ornamentImages = [
    pygame.transform.scale( pygame.image.load(r'images/orn1.png'), ornsize),
    pygame.transform.scale( pygame.image.load(r'images/orn2.png'), ornsize),
    pygame.transform.scale( pygame.image.load(r'images/orn3.png'), ornsize),
    pygame.transform.scale( pygame.image.load(r'images/orn4.png'), ornsize),
    pygame.transform.scale( pygame.image.load(r'images/orn5.png'), ornsize),
    pygame.transform.scale( pygame.image.load(r'images/orn6.png'), ornsize),
    pygame.transform.scale( pygame.image.load(r'images/orn7.png'), ornsize),
]


random.seed(1)

font1 = pygame.font.Font('fonts/notosanskr-bold.otf', 60) 
# font1.set_bold(True)
font2 = pygame.font.Font('fonts/notosanskr.ttf', 25)
font22 = pygame.font.Font('fonts/notosanskr-bold.otf', 30)
#font22.set_bold(True)
font3 = pygame.font.Font('fonts/anton.ttf', 80)
font3.set_italic(True)
font4 = pygame.font.Font('fonts/anton.ttf', 30)

text1 = font1.render("텀블러 사용으로 나무가", True, WHITE)
text2 = font1.render("푸르러질 수 있게", True, WHITE)
text3 = font1.render("도와주세요!", True, WHITE)

text4 = font22.render("목표 달성 :", True, WHITE)

text5 = font4.render("↑ COFFEE CUP TREE", True, GRAY2)

text6 = font2.render("Please, help the tree get green with", True, WHITE)
text7 = font2.render("the use of your own tumbler!", True, WHITE)


#screen = pygame.display.set_mode([1600, 1200], pygame.FULLSCREEN) 
screen = pygame.display.set_mode([1920, 1200], pygame.RESIZABLE) # use only by 1600

clock = pygame.time.Clock()

target_cnt = 30 # FIX HERE
current_cnt = 0
ratio = 0.0
def updateRatio():
    global ratio
    ratio = current_cnt / target_cnt

"""
make leaves
"""
def getXRange(r):
    return (100 + 375*r, 850-370*r)
def getY(r):
    return max([950 - 750*r, 300])

numLeaves = 500
leaves = []
population = [ 0.1* i for i in range(1,10)]
weights = [ (10-i)**2 for i in range(1,10) ]
for i in range(numLeaves):
    randRatio = random.choices(population, weights=weights)
    r = randRatio[0] + random.random()*0.2-0.1
    y = getY(r)
    xr = getXRange(r)
    x = random.uniform( xr[0], xr[1])
    leaves.append( (r,int(x)-20,int(y)-30,random.choice([i for i in range(len(leafImages))])) )
#leaves = sorted(leaves, key=lambda v: -v[0],)

"""
make ornaments
"""
numOrns = 100
ornaments = []

for i in range(numOrns):
    randRatio = random.choices(population, weights=weights)
    r = randRatio[0] + random.random()*0.2-0.1
    y = getY(r)
    xr = getXRange(r)
    x = random.uniform( xr[0], xr[1])
    ornaments.append( (r, int(x)-20,int(y)-30, random.choice([i for i in range(len(ornamentImages))]) ) )


"""
Tree
"""
riseinterval = 10
def drawTree():
    # screen.blit(image, (200, 675 - current_cnt*riseinterval)) # center: 400
    # draw star

    if( current_cnt >= target_cnt ):
        screen.blit(starback, (285,60))

    screen.blit(image, ( 100, 200))
    screen.blit(treebase, (420,1080))

"""
Cups
"""
def drawCups():
    
    for i in leaves[:int(ratio*numLeaves)]:
        #if(i[0] < ratio):
        screen.blit(leafImages[i[3]], (i[1],i[2]))

    screen.blit( stars[min(int(ratio*5),4)], (425, 200) )

    if current_cnt>=target_cnt:
        for i in ornaments[:min(current_cnt-target_cnt, 99)]:
            screen.blit(ornamentImages[i[3]], (i[1],i[2]))


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
slowdown = 1    # 2, 3..
snowradius = 5
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
        pygame.draw.circle(screen, WHITE, i[:2], snowradius)
        
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

    xbase = 950
    ybase = 350
    yinterval = 80
    screen.blit(text1, [xbase, ybase])
    screen.blit(text2, [xbase, ybase+yinterval])
    screen.blit(text3, [xbase, ybase+yinterval+yinterval])

    screen.blit(text4, [xbase, 720])

    screen.blit(text6, [xbase, 600])
    screen.blit(text7, [xbase, 635])

    textnumber = font3.render(f"{current_cnt}",True,YELLOW)
    
    screen.blit(textnumber, [xbase, 760])
    textbase = font3.render(f"/ {target_cnt}",True,WHITE)
    screen.blit(textbase, [xbase+100, 760])

    screen.blit(text5, [50, 1150])


"""
Main Logic
"""

def down():
    global current_cnt
    current_cnt = max(0, current_cnt-1)
    updateRatio()

def up():
    global current_cnt
    current_cnt = current_cnt+1
    updateRatio()

def right():
    global target_cnt
    target_cnt = target_cnt+1
    updateRatio()

def left():
    global target_cnt
    target_cnt = max(0, target_cnt-1)
    updateRatio()
    

running = True
flag=False
while running:

	# handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not flag and event.key == pygame.K_UP:
                up()
            if not flag and event.key == pygame.K_DOWN:
                down()
            if not flag and event.key == pygame.K_LEFT:
                left()
            if not flag and event.key == pygame.K_RIGHT:
                right()
            flag=True
            
        if event.type == pygame.KEYUP:
            flag=False
        
        # TODO keyboard up
        # TODO keyboard down

    # check count updates

	# update elements
    screen.fill((0, 0, 0))

	# draw surface
    #drawBottom()
    drawTree()
    drawCups()
    drawSnow()
    drawDesc()

	# make clock tick 
    clock.tick(60)

	# show surface
    pygame.display.flip()

pygame.quit()

#pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)