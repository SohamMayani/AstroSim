#importing libraries
import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy
import math

#importing from files


#functions for defining shapes
def vector(v1, v2, v3):
    tempVector = numpy.array[v1, v2, v3]
    return tempVector

def triangleCoordinates(xOrigin, yOrigin, zOrigin):
    triangleVerticies = numpy.array([xOrigin, yOrigin, zOrigin])
    return triangleVerticies




# Defining a plane using normal vector
def planeCreator(centerX, centerY, centerZ, normVector):
    if (len(normVector == 3)):
        scalarEq = normVector[0]*centerX + normVector[1]*centerY + normVector[2]*centerZ
        return scalarEq
    else:
        return 0

# Fibonacci sphere, returning a matrix with first row = center coordinates --> Idea by Theo
def fibonacciSphere(numPoints, centerX, centerY, centerZ, scale):
    coordPoints = [[centerX, centerY, centerZ]]
    phi = math.pi*(3 - math.sqrt(5))

    for i in range(numPoints):
        pointZ = 1 - ((2 * i) / (numPoints - 1))
        radius = math.sqrt(1 - (pointZ ** 2))
        rotationAngle = i * phi
        pointX = radius * math.cos(rotationAngle)
        pointY = radius * math.sin(rotationAngle)

        tempX = centerX + (scale * pointX)
        tempY = centerY + (scale * pointY)
        tempZ = centerZ + (scale * pointZ)
        coordPoints.append([tempX, tempY, tempZ])

    return numpy.array(coordPoints, dtype=numpy.float32)

# Matrix coordinates to drawing OpenGL lines
def drawPoly(matrix):
    if numpy.shape(matrix)[0] > 1:
        center = numpy.array(matrix[0])
        glBegin(GL_LINES)

        for i in range(-1 + numpy.shape(matrix)[0]):
            glVertex3fv(matrix[i + 1])

        glEnd()

# Base Icosahedron Generator
def icosahedron(centerX, centerY, centerZ, scale):
    allPoints = [[centerX, centerY, centerZ]]
    phi = (1 + math.sqrt(5)) / 2
    negative = [[1, 1, 1], [-1, 1, 1], [1, -1, 1], [1, 1, -1], [-1, -1, 1], [-1, 1, -1], [1, -1, -1], [-1, -1, -1]]
    point = [0, 1, phi]
    for i in range(3):
        for j in range(8):
            pointX = scale * point[i % 3] * negative[j][0]
            pointY = scale * point[(i + 1) % 3] * negative[j][1]
            pointZ = scale * point[(i + 2) % 3] * negative[j][2]
            allPoints.append([centerX + pointX, centerY + pointY, centerZ + pointZ])

    coordPoints = []
    for i in allPoints:
        if i not in coordPoints:
            coordPoints.append(i)

    return numpy.array(coordPoints, dtype=numpy.float32)


# Cross product for 3D vectors
def crossProduct(v1, v2):
    if (len(v1) == len(v2)):
        c1 = v1[1]*v2[2] - v2[1]*v1[2]
        c2 = v1[2]*v2[0] - v2[2]*v1[0]
        c3 = v1[0]*v2[1] - v2[0]*v1[1]
        crossProduct = numpy.array[c1, c2, c3]
        return crossProduct
    else:
        return 0



# Dot product for nD vectors
def dotProduct(v1, v2):
    if (len(v1) == len(v2)):
        vectorC = []
        for i in range(0, len(v1)):
            vectorC.append(v1[i] + v2[i])
        
        dotProduct = numpy.array[vectorC]
        return dotProduct
    else:
        return 0