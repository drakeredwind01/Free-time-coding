import pygame

pygame.init()

width = 300
height = 200

cols = width
rows = height

#dampening = how fast the ripple effect stops.
dampening = 0.999

#Arrays that hold the colors of the screen.
current = [[0]*rows for col in range(cols)]
previous = [[0]*rows for col in range(cols)]

print(current[0][0], current[199][199])

screen = pygame.display.set_mode((width,height))
#Sets the initial background to black
screen.fill((0,0,0))

img = pygame.Surface((width, height))

#Mainloop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    if any(pygame.mouse.get_pressed()):
        mouse_pos = pygame.mouse.get_pos()
        previous[mouse_pos[0]][mouse_pos[1]] = 500

    #This part seems to be the problem
    pixelArray = pygame.PixelArray(img)
    for i in range(1,cols-1):
        for j in range(1,rows-1):
            current[i][j] = (
                previous[i-1][j] +
                previous[i+1][j] +
                previous[i][j-1] +
                previous[i][j+1]) / 2 - current[i][j]
            current[i][j] *= dampening
            val = min(255, max(0, round(current[i][j])))
            pixelArray[i, j] = (val, val, val)
    pixelArray.close()

    # Switching the arrays
    previous, current = current, previous

    screen.blit(img, (0, 0))
    pygame.display.flip()
