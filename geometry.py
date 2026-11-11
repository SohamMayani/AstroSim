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

    coordPoints = removeDuplicateArray(allPoints)
    coordPoints = orderingVectors(removeDuplicateArray(allPoints))
    return numpy.array(coordPoints, dtype=numpy.float32)

# Removal of repeated array elements
def removeDuplicateArray(array):
    relist = [array[0]]
    for i in array:
        if i not in relist:
            relist.append(i)
    return relist

# Removal of of overlapping line coordinates (a->b and b->a contribute the same line)
def removeDuplicateLine(matrix):
    if (numpy.shape(matrix)[1] != 3):
        print("There was an error with the removeDuplicateLine Function input")
        return -1
    else:
        relist = [matrix[0]]
        for i in range(1, numpy.shape(matrix)[0] - 1):
            for j in range(2, numpy.shape(matrix)[0]):
                if (i != j) and ([matrix[i], matrix[i+1]] != [matrix[j], matrix[j-1]]):
                    relist.append(matrix[i])

        return relist


# Dot product for n-D vectors
def dotProduct(v1, v2):
    if (len(v1) == len(v2)):
        vectorC = []
        for i in range(0, len(v1)):
            vectorC.append(v1[i] + v2[i])
        
        dotProduct = numpy.array[vectorC]
        return dotProduct
    else:
        return 0

# Adds vectors, scaled if necessary
def vectorAdd(v1, v2, scale1=1, scale2=1):
    if (len(v1) == len(v2)):
        sumVector = []
        for i in range(0, len(v1)):
            sumVector.append((scale1*v1[i]) + (scale2*v2[i]))

        return sumVector

# Computes the distance between vectors
def vectorDistance(v1, v2):
    if len(v1) == len(v2):
        distance = 0.0
        for i in range(0, len(v1)):
            distance += pow(v1[i] - v2[i], 2)

        return math.sqrt(distance)
    else:
        print("There was an error with the vectorDistance function")
        return -1

# Computes shortest distance between vectors in a matrix (not including center/first entry in matrix)
def shortestDistance(matrix):
    currentShort = vectorDistance(matrix[1], matrix[2])
    if numpy.shape(matrix)[1] == 3:
        for i in range(1, len(matrix)):
            for j in range (1, len(matrix)):
                if (i != j) and (vectorDistance(matrix[i], matrix[j]) < currentShort):
                    currentShort = vectorDistance(matrix[i], matrix[j])
        return currentShort
    else:
        print("orderIcosaLines received improper input")
        return -1

# Rearranges and duplicates vectors in a matrix so that nearby vectors are adjacent
def orderingVectors(matrix):
    if numpy.shape(matrix)[1] != 3:
        print("Incorrect shape for orderingVectors input")
        return -1
    else:
        shortDistance = shortestDistance(matrix)
        reorderedList = [[]]
        for i in range(1, numpy.shape(matrix)[0]):
            for j in range(1, numpy.shape(matrix)[0]):
                if (i != j) and (vectorDistance(matrix[i], matrix[j]) == shortDistance):
                    reorderedList.append(matrix[i])
                    reorderedList.append(matrix[j])
        print(reorderedList)
        return removeDuplicateLine(reorderedList)

# # Ordering pairs of coordinates using dot products (inputs 2d matrix)
# def orderedCoords(matrix):
#     if len(numpy.shape(matrix)) == 2:
#         center = matrix[0]
#         dotProdlist = []
#         pointsList = [[]]
#         for v1 in matrix:
#             for v2 in matrix:
#                 if (v1.all() != v2.all()):
#                     dotProdlist.append(dotProduct(vectorAdd(center, v1, -1), vectorAdd(center, v2, -1)))
#                     pointsList.append([v1, v2])

#         maxDotProd = 0
#         for index1 in dotProdlist:
#             if maxDotProd < dotProdlist[index1]:
#                 maxDotProd = dotProdlist[index1]


#         neighborPoints = [[]]

#         for index2 in range(len(dotProdlist)):
#             if dotProdlist[index2] is maxDotProd:
#                 neighborPoints.append(pointsList[index2][0])
#                 neighborPoints.append(pointsList[index2][1])

#         return removeDuplicateLine(neighborPoints)
#     else:
#         print("There was an error with the orderedCoords Function input")
#         return -1

# # Cross product for 3D vectors
# def crossProduct(v1, v2):
#     if (len(v1) == len(v2)):
#         c1 = v1[1]*v2[2] - v2[1]*v1[2]
#         c2 = v1[2]*v2[0] - v2[2]*v1[0]
#         c3 = v1[0]*v2[1] - v2[0]*v1[1]
#         crossProduct = numpy.array[c1, c2, c3]
#         return crossProduct
#     else:
#         return 0