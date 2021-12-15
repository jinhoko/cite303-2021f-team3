import pygame
import random

"""
Assets
"""
pygame.init()
WHITE = (255,255,255)
BLACK = (0,0,0)
image = pygame.image.load(r'images/tree1.png')
# image = pygame.transform.scale(image, (200,400))

#screen = pygame.display.set_mode([1920, 1080], pygame.FULLSCREEN) 
screen = pygame.display.set_mode([1920, 1080])

clock = pygame.time.Clock()
"""
Tree
"""
def drawTree():
    screen.blit(image, (100, 100))

"""
Snow
"""
snowflakes = []
numSnow = 100
snowX1 = 0
snowX2 = 1920
snowY1 = 0
snowY2 = 1080
randSpeed = [2,3]
slowdown = 5    # 2, 3..
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
        pygame.draw.circle(screen, WHITE, i[:2], 3)
        
        if i[1] > snowY2:
            i[0] = random.randrange(snowX1, snowX2) 
            i[1] = random.randrange(-50 + snowY1, -5 + snowY1)

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

	# update elements
    screen.fill((0, 0, 0))

	# draw surface
    drawTree()
    drawSnow()

	# make clock tick 
    clock.tick(60)

	# show surface
    pygame.display.flip()

pygame.quit()

#pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)