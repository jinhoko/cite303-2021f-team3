import pygame

# init assets
pygame.init()
image = pygame.image.load(r'images/tree1.png')
# image = pygame.transform.scale(image, (200,400))


screen = pygame.display.set_mode([1920, 1680], pygame.FULLSCREEN)
running = True
while running:

	# handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

	# update elements
    screen.fill((0, 0, 0))

	# draw surface
    #pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    screen.blit(image, (100, 100))


	# make clock tick 

	# show surface
    pygame.display.flip()

pygame.quit()