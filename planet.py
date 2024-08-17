
# Import and initialize the pygame library

import pygame

pygame.init()


# Set up the drawing window

screen = pygame.display.set_mode([1200, 600])


# Run until the user asks to quit

running = True

while running:


    # Did the user click the window close button?

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            running = False
        


    # Fill the background 

    


    # Draw a solid blue circle in the center

    for i in range(1000):
        screen.fill((i+20, 255, i+10))
        print('.............')
        pygame.draw.circle(screen, (i, i, 255), (100, 250), i)
        pygame.draw.circle(screen, (i, i, i), (250, 250), i)
        pygame.draw.polygon(screen,[255,0,0],[(300,200),(400,200),(600,300),(500,300)])
        pygame.draw.line(screen,[255,255,255],(i,300),(900,800))
        pygame.draw.lines(screen,(0, 0, 255),True,[(i,50),(70,60),(200,200)])
        pygame.draw.rect(screen,[i,i,i],(240,200,300,300),width=i)
        screen.scroll(600,300)
        pygame.display.update()
        print(pygame.display.get_surface())

        if i>=200:
            break
        


    # Flip the display

    pygame.display.flip()


# Done! Time to quit.

pygame.quit()
