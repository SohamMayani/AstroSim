import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

# 1. Define the 8 corner vertices of a 3D cube (X, Y, Z coordinates)
vertices = (
    (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, -1),
    (1, -1, 1),  (1, 1, 1),  (-1, -1, 1),  (-1, 1, 1)
)

# 2. Define the 12 edges connecting those vertices together
edges = (
    (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
    (6,3), (6,4), (6,7), (5,1), (5,4), (5,7)
)

def DrawCube():
    """Tells OpenGL to render lines between our defined vertices."""
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

