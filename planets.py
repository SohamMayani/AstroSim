# Importing Libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

# Importing from files
from shapes import *

class AstronomicalObject:
    # Construction
    def __init__(self, type, center, size, shape, momentum):
        self._type = type
        self._center = [center[0], center[1], center[2]]
        self._size = size
        self.create_shape(shape)
        self._momentum = momentum

    # Instance Methods
    # Draw Astronomical Object
    def draw(self):
        glBegin(GL_LINES)
        for i in range(0, len(self._shape.edges)):
            glVertex3fv(self.addVector(self._shape.edges[i], self._center))
        glEnd()
        self.update()

    # Define the coordinates for the Astronomical Object
    def create_shape(self, shape):
        if (shape == "cube"):
            self._shape = Cube()
        elif (shape == "icosahedron"):
            self._shape = Icosahedron()
        self._shape.set_size(self._size)

    # Update Astronomical Object
    def update(self):
        self._center = self.addVector(self._center, self._momentum)
        self._momentum = self.addVector(self._momentum, self.scaleVector(self._center, -0.001))
    # Astronomical Object Physics??? (Ignore this comment, unsure about implementing physics in this class, or creating another)

    # Static Methods
    # Vector Addition
    @staticmethod
    def addVector(v1, v2):
        if (len(v1) != len(v2)):
            raise ValueError(f"Cannot add vectors of different lengths:\n{v1} and {v2}")
        v0 = []
        for i in range(0, len(v1)):
            v0.append(v1[i] + v2[i])
        return v0

    @staticmethod
    def scaleVector(v1, scalar):
        v0 = []
        for i in range(0, len(v1)):
            v0.append(scalar * v1[i])
        return v0


class Star(AstronomicalObject):
    # Construction
    def __init__(self, name, center=[0, 0, 0], size=1, shape="cube", momentum=[0, 0, 0]):
        if (not isinstance(name, str)):
            raise NotImplementedError("Creating a star requires a name")
        self._name = name
        # if ((len(center) != 3) or (not (isinstance(size, float)) or (isinstance(size, int))) or (not isinstance(shape, str)) or (len(momentum) != 3)):
        #     raise ValueError(f"Incorrect inputs were received when trying to create the star {self._name}")
        super().__init__("star", center, size, shape, momentum)

    # Properties (getters)
    @property
    def name(self):
        return self._name

class Planet:
    def __init__(self, name, center, size):
        
        if ((np.shape(center)[1] != 3) or (not isinstance(name, str)) or (not isinstance(size, int))):
            raise ValueError(f"Incorrect attempt at defining {self.name}, please check inputs!")
        
        self.__name = name
        self.__center = [center[0], center[1], center[2]]
        self.__size = size

        self.__weight = size ** 3
        self.__momentum = [self.__weight, 0, 0, 0]

    def __str__(self):
        return f"{name}"

    def __add__(self):
        return self.__weight

    def __call__(self, call="none"):
        if (call == "none" or call == "center"):
            return self.__center
        elif (call == "name"):
            return self.__name
        elif (call == "size"):
            return self.__size
        else:
            print("That is not a recognized property of this Planet")
            return -1



# Non-fundamental functions of class Planet
# Getters
    def get_weight(self):
        return self.__weight

    def get_momentum(self):
        return self.__momentum

# Setters
    def set_momentum(self, vector):
        if (not isinstance(vector, list)):
            print(".set_momentum recieved the wrong type of input")
            return -1
        else:
            self.__momentum = [self.__weight, vector[0], vector[1], vector[2]]
            return self.__momentum

    def change_momentum(self, vector):
        if (not isinstance(vector, list)):
            print(".change_momentum recieved the wrong type of input")
            return -1
        else:
            self.__momentum[1] += vector[1]
            self.__momentum[2] += vector[2]
            self.__momentum[3] += vector[3]
            return self.__momentum

# Other functions
# draw() will assume that it is called under glBegin(GL_Lines)
    def draw(self, shape):
        if ((np.shape(shape)[1] != 3) or (len(np.shape(shape)) != 2)):
            print(f"The planet {self.__name} cannot be drawn with this shape")
        else:
            for i in range(0, len(np.shape(shape)[0])):
                x = shape[i][0] + self.__center[0]
                y = shape[i][1] + self.__center[1]
                z = shape[i][2] + self.__center[2]
                glVertex3fv([x, y, z])

