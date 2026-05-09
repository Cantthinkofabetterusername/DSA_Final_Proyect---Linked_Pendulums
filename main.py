import pygame
from pygame.locals import *
from graphics_functions import *
from linked_list import LinkedList

def main():
    pygame.init()
    display = [1728, 1117]
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glFrustum(-0.0128, 0.0128, -0.0083, 0.0083, 0.02, 1000)
    glTranslatef(0, 0, -5)
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()
        glClearColor(0.2, 0.3, 0.3, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        generateCircle(0, 0, 360, 0.2)
        pygame.display.flip()
        pygame.time.wait(10)

main()