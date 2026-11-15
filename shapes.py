#importing libraries
import numpy as np
import math

# Parent class of all Shapes
class Shape:
    # Construction
    def __init__(self, name, vertices):
        if len(vertices) < 2 or np.shape(vertices)[1] != 3:
            raise ValueError("The shape did not receive enough vertices, or the shape does not have 3-D coordinates")
        self._name = name
        self._vertices = vertices
        self._edges = None

    # Methods
    def organizer(self):
        organizedVertices = []
        numPoints = len(self._vertices)
        adjacent = self.minDist()
    
        for i in range(0, numPoints):
            for j in range(i + 1, numPoints):
                dist = self.distance(self._vertices[i], self._vertices[j])
                if (math.isclose(dist, adjacent, abs_tol = 1e-6)):
                    organizedVertices.append(list(self._vertices[i]))
                    organizedVertices.append(list(self._vertices[j]))
        return organizedVertices

    def minDist(self):
        numPoints = len(self._vertices)
        minimum = self.distance(self._vertices[0], self._vertices[1])
        for i in range(0, numPoints):
            for j in range(i + 1, numPoints):
                dist = self.distance(self._vertices[i], self._vertices[j])
                if (dist < minimum):
                    minimum = dist
        return minimum

    @staticmethod
    def distance(vertex1, vertex2):
        if (len(vertex1) != len(vertex2)):
            raise ValueError("Could not compute the distance between arrays of different sizes")
        
        dist = 0
        for i in range(0, len(vertex1)):
            dist += (vertex1[i] - vertex2[i]) ** 2
        return math.sqrt(dist)

    # Mutators
    def set_size(self, size):
        for vertex in range(0, len(self._vertices)):
            for dimension in range(0, len(self._vertices[vertex])):
                self._vertices[vertex][dimension] *= size

    # Properties (accessors)
    @property
    def name(self):
        return self._name

    @property
    def vertices(self):
        return [list(vertex) for vertex in self._vertices]

    @property
    def edges(self):
        if self._edges is None:
            self._edges = self.organizer()
        return self._edges

# Icosahedron, a child of Shape
class Icosahedron(Shape):
    def __init__(self):
        super().__init__("icosahedron", self.createIcosahedron())

    def createIcosahedron(self):
        icosa = []
        phi = (1 + math.sqrt(5)) / 2

        for sign1 in (1, -1):
            for sign2 in (1, -1):
                point = [0, sign1 * 1, sign2 * phi]
                for i in range(3):
                    pointX = point[i % 3]
                    pointY = point[(i + 1) % 3]
                    pointZ = point[(i + 2) % 3]
                    icosa.append([pointX, pointY, pointZ])
        return icosa

class Cube(Shape):
    def __init__(self):
        super().__init__("cube", self.createCube())

    def createCube(self):
        cube = []

        for x in (-1, 1):
            for y in (-1, 1):
                for z in (-1, 1):
                    cube.append([x, y, z])
        return cube