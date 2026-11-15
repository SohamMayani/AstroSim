# Importing Libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# Importing from files
from planets import *
from shapes import *


def main():

    test = Star("Test", [0, 0, 8], 0.2, "icosahedron")
    test2 = Star("Test2", [-2, -2, -2], 0.5, "icosahedron")
    test3 = Star("Test3", [-8, 2, 2], 1, "cube", [0.1, 0, 0])

    pygame.init()
    display = (1600, 900)
    # Tell Pygame we are using OpenGL for this window
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # Configure the 3D Perspective Camera
    # gluPerspective(Field of View, Aspect Ratio, Near Clipping Plane, Far Clipping Plane)
    gluPerspective(45, (display[0] / display[1]), 0.1, 250.0)
    
    # Move the camera back 5 units along the Z axis so we can see the cube
    glTranslatef(0.0, 0.0, -44.0)

    clock = pygame.time.Clock()

    # The Continuous Game Loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Rotate the cube by 1 degree around the (X=1, Y=1, Z=1) axis vector per frame
        glRotatef(1, 1, 0, 1)
        
        # Clear the screen's color buffer and depth buffer before drawing the new frame
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        test.draw()
        test2.draw()
        test3.draw()
        
        pygame.display.flip()
        clock.tick(60) # Limit the simulation to 60 FPS

if __name__ == "__main__":
    main()
