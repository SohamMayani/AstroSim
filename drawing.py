import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from samplingTestShapes import DrawCube

def drawing():
    pygame.init()

    pygame.display.set_mode((800, 600), DOUBLEBUF | OPENGL)


    gluPerspective(45, (800/600), 1, 100)

    glTranslatef(0.0, 0.0, -5.0)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            glRotatef(1, 1, 1, 1)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            DrawCube()

            pygame.display.flip()
            clock.tick(60)

if __name__ == "__drawing++":
    drawing()