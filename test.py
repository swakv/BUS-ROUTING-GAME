import pygame, time

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
blue = (0,0,255)

def button(x,y,w,h,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        if click [0] == 1 and action != None:
            if action == "exit":
                pygame.quit()
                quit()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

gameExit = False

logo1 = pygame.image.load('logo.png')  # Don't load these in a loop!
# logo2 = pygame.image.load('logo2.png') # Only need to load them once.

# Make sure you record start_time here! Because the timer actually
# started several seconds before the display is ready.

start_time = pygame.time.get_ticks() / 1000

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True

    time = pygame.time.get_ticks() / 1000
    elapsed = time - start_time

    gameDisplay.fill(black)

    if elapsed > 4:
        gameDisplay.fill(white)
        button(0, 0, 10, 10, 'exit')
        pygame.draw.rect(gameDisplay, red, (0, 0, 10, 10))
    # elif elapsed > 2:
    #     gameDisplay.blit(logo2, (0, 0))
    elif elapsed > 0:
        gameDisplay.blit(logo1, (1, 1))

    pygame.display.update()
    clock.tick(15)

pygame.quit()
quit()