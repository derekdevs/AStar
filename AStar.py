
'''
 @author Derek Walker
 A* Simulation
 Simulates A*, a path-finding and graph traversing algorithm.
 March 26, 2014
'''

import pygame
import sys

# Define a Square object
class Square:
    def __init__(self, y, x, squareType, color):
        self.xVal = x
        self.yVal = y
        self.squareType = squareType
        self.color = color
    def getX(self):
        return self.xVal
    def getY(self):
        return self.yVal
    def getSquareType(self):
        return self.squareType
    def getF(self):
        return self.fVal
    def getG(self):
        return self.gVal
    def getH(self):
        return self.hVal
    def getColor(self):
        return self.color
    def getXCoordinate(self):
        self.xCoord = int(self.xVal/width)
        return self.xCoord
    def getYCoordinate(self):
        self.yCoord = int(self.yVal/height)
        return self.yCoord
    def getPosition(self):
        self.position = self.getYCoordinate(), self.getXCoordinate()
        return (self.position)
    def getParent(self):
        return self.parent
    def setF(self, fVal):
        self.fVal = fVal
    def setG(self, gVal):
        self.gVal = gVal
    def setH(self, hVal):
        self.hVal = hVal
    def setY(self, yVal):
        self.yVal = yVal
    def setParent(self, square):
        self.parent = square

def determineSquareType():
    # Top wall
    if currentSquare.getYCoordinate() == 0:
        if currentSquare.getXCoordinate() == 0:
            adjacentType = "top left"
        elif currentSquare.getXCoordinate() < maxXCoordinate:
            adjacentType = "top middle"
        elif currentSquare.getXCoordinate() == maxXCoordinate:
            adjacentType = "top right"
    # Middle wall
    elif currentSquare.getYCoordinate() < maxYCoordinate:
        if currentSquare.getXCoordinate() == 0:
            adjacentType = "mid left"
        elif currentSquare.getXCoordinate() < maxXCoordinate:
            adjacentType = "mid middle"
        elif currentSquare.getXCoordinate() == maxXCoordinate:
            adjacentType = "mid right"
    # Bottom wall
    elif currentSquare.getYCoordinate() == maxYCoordinate:
        if currentSquare.getXCoordinate() == 0:
            adjacentType = "bottom left"
        elif currentSquare.getXCoordinate() < maxXCoordinate:
            adjacentType = "bottom middle"
        elif currentSquare.getXCoordinate() == maxXCoordinate:
            adjacentType = "bottom right"
    
    return adjacentType

def topLeft():
    for row in range(numRows):
        for column in range(numCols):
            # Top left square
            if squares[row][column].getYCoordinate() == currentSquare.getYCoordinate()-1 and squares[row][column].getXCoordinate() == currentSquare.getXCoordinate()-1:
                # Check for obstacle in the way
                if squares[row+1][column].getSquareType() != "obstacle" and squares[row][column+1].getSquareType() != "obstacle":
                    # Check if this square is an obstacle
                    if squares[row][column].getSquareType() != "obstacle":
                        # Check that the square is not on the closed list already
                        isNotOnClosedList = "True"
                        for x in range(0, len(closedList)):
                            if closedList[x].getYCoordinate() == squares[row][column].getYCoordinate() and closedList[x].getXCoordinate() == squares[row][column].getXCoordinate():
                                isNotOnClosedList = "False"
                        if isNotOnClosedList == "True":
                            # Set F and G values; add adjacent square to openList
                            onOpenList = "False"
                            for y in range(0, len(openList)):
                                if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                    onOpenList = "True"
                                    # If not already on open list, set G
                            if onOpenList == "False":
                                squares[row][column].setG(currentSquare.getG() + 14)
                            glabel = myfont.render(str(squares[row][column].getG()), 1, WHITE)
                            screen.blit(glabel, (squares[row][column].getX() + width/6,
                                    squares[row][column].getY() + height - height/3))
                            # F = G + H
                            squares[row][column].setF(squares[row][column].getG() + squares[row][column].getH())
                            flabel = myfont.render(str(squares[row][column].getF()), 1, WHITE)
                            screen.blit(flabel, (squares[row][column].getX() + width/6, 
                                    squares[row][column].getY() + height/6))
                            isOnOpenList = "False"
                            for y in range(0, len(openList)):
                                if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                    isOnOpenList = "True"
                            # If the square is not on the open list, add it
                            if isOnOpenList == "False":
                                openList.append(squares[row][column])
                                squares[row][column].setParent(currentSquare)
                            # If the square is on the open list, check to see if this new path is better using the G value
                            # Lower G => better path
                            elif isOnOpenList == "True":
                                oldG = squares[row][column].getG()
                                newG = currentSquare.getG() + 14
                                # Reset G value because this is a better path, change parent to current square, reset G and F values
                                if oldG > newG:
                                    squares[row][column].setG(newG)
                                    squares[row][column].setF(newG + squares[row][column].getH())
                                    # Change parent to current square
                                    squares[row][column].setParent(currentSquare)
def top():
    for row in range(numRows):
        for column in range(numCols):
            # Top square
            if squares[row][column].getYCoordinate() == currentSquare.getYCoordinate()-1 and squares[row][column].getXCoordinate() == currentSquare.getXCoordinate():
                # Check if this square is an obstacle
                if squares[row][column].getSquareType() != "obstacle":
                    # Check that the square is not on the closed list already
                    isNotOnClosedList = "True"
                    for x in range(0, len(closedList)):
                        if closedList[x].getYCoordinate() == squares[row][column].getYCoordinate() and closedList[x].getXCoordinate() == squares[row][column].getXCoordinate():
                            isNotOnClosedList = "False"                 
                    if isNotOnClosedList == "True":
                        # Set F and G values; add adjacent square to openList
                        onOpenList = "False"
                        for y in range(0, len(openList)):
                            if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                onOpenList = "True"
                        # If not already on open list, set G
                        if onOpenList == "False":
                            squares[row][column].setG(currentSquare.getG() + 10)
                        glabel = myfont.render(str(squares[row][column].getG()), 1, WHITE)
                        screen.blit(glabel, (squares[row][column].getX() + width/6, 
                                squares[row][column].getY() + height - height/3))
                        # F = G + H
                        squares[row][column].setF(squares[row][column].getG() + squares[row][column].getH())
                        flabel = myfont.render(str(squares[row][column].getF()), 1, WHITE)
                        screen.blit(flabel, (squares[row][column].getX() + width/6, 
                                squares[row][column].getY() + height/6))
                        isOnOpenList = "False"
                        for y in range(0, len(openList)):
                            if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                isOnOpenList = "True"
                        # If the square is not on the open list, add it
                        if isOnOpenList == "False":
                            openList.append(squares[row][column])
                            squares[row][column].setParent(currentSquare)
                        # If the square is on the open list, check to see if this new path is better using the G value
                        # Lower G => better path
                        elif isOnOpenList == "True":
                            oldG = squares[row][column].getG()
                            newG = currentSquare.getG() + 10
                            # Reset G value because this is a better path, change parent to current square, reset G and F values
                            if oldG > newG:
                                squares[row][column].setG(newG)
                                squares[row][column].setF(newG + squares[row][column].getH())
                                # Change parent to current square
                                squares[row][column].setParent(currentSquare)
def topRight():
    for row in range(numRows):
        for column in range(numCols):
            # Top right square
            if squares[row][column].getYCoordinate() == currentSquare.getYCoordinate()-1 and squares[row][column].getXCoordinate() == currentSquare.getXCoordinate()+1:
                # Check for obstacle in the way
                if squares[row][column-1].getSquareType() != "obstacle" and squares[row+1][column].getSquareType() != "obstacle":
                    # Check if this square is an obstacle
                    if squares[row][column].getSquareType() != "obstacle":
                        # Check that the square is not on the closed list already
                        isNotOnClosedList = "True"
                        for x in range(0, len(closedList)):
                            if closedList[x].getYCoordinate() == squares[row][column].getYCoordinate() and closedList[x].getXCoordinate() == squares[row][column].getXCoordinate():
                                isNotOnClosedList = "False"
                        if isNotOnClosedList == "True":
                            # Set F and G values; add adjacent square to openList
                            onOpenList = "False"
                            for y in range(0, len(openList)):
                                if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                    onOpenList = "True"
                                    # If not already on open list, set G
                            if onOpenList == "False":
                                squares[row][column].setG(currentSquare.getG() + 14)
                            glabel = myfont.render(str(squares[row][column].getG()), 1, WHITE)
                            screen.blit(glabel, (squares[row][column].getX() + width/6,
                                    squares[row][column].getY() + height - height/3))
                            # F = G + H
                            squares[row][column].setF(squares[row][column].getG() + squares[row][column].getH())
                            flabel = myfont.render(str(squares[row][column].getF()), 1, WHITE)
                            screen.blit(flabel, (squares[row][column].getX() + width/6, 
                                    squares[row][column].getY() + height/6))
                            isOnOpenList = "False"
                            for y in range(0, len(openList)):
                                if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                    isOnOpenList = "True"
                            # If the square is not on the open list, add it
                            if isOnOpenList == "False":
                                openList.append(squares[row][column])
                                squares[row][column].setParent(currentSquare)
                            # If the square is on the open list, check to see if this new path is better using the G value
                            # Lower G => better path
                            elif isOnOpenList == "True":
                                oldG = squares[row][column].getG()
                                newG = currentSquare.getG() + 14
                                # Reset G value because this is a better path, change parent to current square, reset G and F values
                                if oldG > newG:
                                    squares[row][column].setG(newG)
                                    squares[row][column].setF(newG + squares[row][column].getH())
                                    # Change parent to current square
                                    squares[row][column].setParent(currentSquare)
def left():
    for row in range(numRows):
        for column in range(numCols):
            # Left square
            if squares[row][column].getYCoordinate() == currentSquare.getYCoordinate() and squares[row][column].getXCoordinate() == currentSquare.getXCoordinate()-1:
                # Check if this square is an obstacle
                if squares[row][column].getSquareType() != "obstacle":
                    # Check that the square is not on the closed list already
                    isNotOnClosedList = "True"
                    for x in range(0, len(closedList)):
                        if closedList[x].getYCoordinate() == squares[row][column].getYCoordinate() and closedList[x].getXCoordinate() == squares[row][column].getXCoordinate():
                            isNotOnClosedList = "False"                 
                    if isNotOnClosedList == "True":
                        # Set F and G values; add adjacent square to openList
                        onOpenList = "False"
                        for y in range(0, len(openList)):
                            if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                onOpenList = "True"
                        # If not already on open list, set G
                        if onOpenList == "False":
                            squares[row][column].setG(currentSquare.getG() + 10)
                        glabel = myfont.render(str(squares[row][column].getG()), 1, WHITE)
                        screen.blit(glabel, (squares[row][column].getX() + width/6, 
                                squares[row][column].getY() + height - height/3))
                        # F = G + H
                        squares[row][column].setF(squares[row][column].getG() + squares[row][column].getH())
                        flabel = myfont.render(str(squares[row][column].getF()), 1, WHITE)
                        screen.blit(flabel, (squares[row][column].getX() + width/6, 
                                squares[row][column].getY() + height/6))
                        isOnOpenList = "False"
                        for y in range(0, len(openList)):
                            if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                isOnOpenList = "True"
                        # If the square is not on the open list, add it
                        if isOnOpenList == "False":
                            openList.append(squares[row][column])
                            squares[row][column].setParent(currentSquare)
                        # If the square is on the open list, check to see if this new path is better using the G value
                        # Lower G => better path
                        elif isOnOpenList == "True":
                            oldG = squares[row][column].getG()
                            newG = currentSquare.getG() + 10
                            # Reset G value because this is a better path, change parent to current square, reset G and F values
                            if oldG > newG:
                                squares[row][column].setG(newG)
                                squares[row][column].setF(newG + squares[row][column].getH())
                                # Change parent to current square
                                squares[row][column].setParent(currentSquare)
def right():
    for row in range(numRows):
        for column in range(numCols):
            # Right square
            if squares[row][column].getYCoordinate() == currentSquare.getYCoordinate() and squares[row][column].getXCoordinate() == currentSquare.getXCoordinate()+1:
                # Check if this square is an obstacle
                if squares[row][column].getSquareType() != "obstacle":
                    # Check that the square is not on the closed list already
                    isNotOnClosedList = "True"
                    for x in range(0, len(closedList)):
                        if closedList[x].getYCoordinate() == squares[row][column].getYCoordinate() and closedList[x].getXCoordinate() == squares[row][column].getXCoordinate():
                            isNotOnClosedList = "False"                 
                    if isNotOnClosedList == "True":
                        # Set F and G values; add adjacent square to openList
                        onOpenList = "False"
                        for y in range(0, len(openList)):
                            if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                onOpenList = "True"
                        # If not already on open list, set G
                        if onOpenList == "False":
                            squares[row][column].setG(currentSquare.getG() + 10)
                        glabel = myfont.render(str(squares[row][column].getG()), 1, WHITE)
                        screen.blit(glabel, (squares[row][column].getX() + width/6, 
                                squares[row][column].getY() + height - height/3))
                        # F = G + H
                        squares[row][column].setF(squares[row][column].getG() + squares[row][column].getH())
                        flabel = myfont.render(str(squares[row][column].getF()), 1, WHITE)
                        screen.blit(flabel, (squares[row][column].getX() + width/6, 
                                squares[row][column].getY() + height/6))
                        isOnOpenList = "False"
                        for y in range(0, len(openList)):
                            if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                isOnOpenList = "True"
                        # If the square is not on the open list, add it
                        if isOnOpenList == "False":
                            openList.append(squares[row][column])
                            squares[row][column].setParent(currentSquare)
                        # If the square is on the open list, check to see if this new path is better using the G value
                        # Lower G => better path
                        elif isOnOpenList == "True":
                            oldG = squares[row][column].getG()
                            newG = currentSquare.getG() + 10
                            # Reset G value because this is a better path, change parent to current square, reset G and F values
                            if oldG > newG:
                                squares[row][column].setG(newG)
                                squares[row][column].setF(newG + squares[row][column].getH())
                                # Change parent to current square
                                squares[row][column].setParent(currentSquare)
def bottomLeft():
    for row in range(numRows):
        for column in range(numCols):
            # Bottom left square
            if squares[row][column].getYCoordinate() == currentSquare.getYCoordinate()+1 and squares[row][column].getXCoordinate() == currentSquare.getXCoordinate()-1:
                # Check for obstacle in the way
                if squares[row-1][column].getSquareType() != "obstacle" and squares[row][column+1].getSquareType() != "obstacle":
                    # Check if this square is an obstacle
                    if squares[row][column].getSquareType() != "obstacle":
                        # Check that the square is not on the closed list already
                        isNotOnClosedList = "True"
                        for x in range(0, len(closedList)):
                            if closedList[x].getYCoordinate() == squares[row][column].getYCoordinate() and closedList[x].getXCoordinate() == squares[row][column].getXCoordinate():
                                isNotOnClosedList = "False"        
                        if isNotOnClosedList == "True":
                            # Set F and G values; add adjacent square to openList
                            onOpenList = "False"
                            for y in range(0, len(openList)):
                                if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                    onOpenList = "True"
                            # If not already on open list, set G
                            if onOpenList == "False":
                                squares[row][column].setG(currentSquare.getG() + 14)
                            glabel = myfont.render(str(squares[row][column].getG()), 1, WHITE)
                            screen.blit(glabel, (squares[row][column].getX() + width/6,
                                    squares[row][column].getY() + height - height/3))
                            # F = G + H
                            squares[row][column].setF(squares[row][column].getG() + squares[row][column].getH())
                            flabel = myfont.render(str(squares[row][column].getF()), 1, WHITE)
                            screen.blit(flabel, (squares[row][column].getX() + width/6, 
                                    squares[row][column].getY() + height/6))
                            isOnOpenList = "False"
                            for y in range(0, len(openList)):
                                if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                    isOnOpenList = "True"
                            # If the square is not on the open list, add it
                            if isOnOpenList == "False":
                                openList.append(squares[row][column])
                                squares[row][column].setParent(currentSquare)
                            # If the square is on the open list, check to see if this new path is better using the G value
                            # Lower G => better path
                            elif isOnOpenList == "True":
                                oldG = squares[row][column].getG()
                                newG = currentSquare.getG() + 14
                                # Reset G value because this is a better path, change parent to current square, reset G and F values
                                if oldG > newG:
                                    squares[row][column].setG(newG)
                                    squares[row][column].setF(newG + squares[row][column].getH())
                                    # Change parent to current square
                                    squares[row][column].setParent(currentSquare)
def bottom():
    for row in range(numRows):
        for column in range(numCols):
            # Bottom square
            if squares[row][column].getYCoordinate() == currentSquare.getYCoordinate()+1 and squares[row][column].getXCoordinate() == currentSquare.getXCoordinate():
                # Check if this square is an obstacle
                if squares[row][column].getSquareType() != "obstacle":
                    # Check that the square is not on the closed list already
                    isNotOnClosedList = "True"
                    for x in range(0, len(closedList)):
                        if closedList[x].getYCoordinate() == squares[row][column].getYCoordinate() and closedList[x].getXCoordinate() == squares[row][column].getXCoordinate():
                            isNotOnClosedList = "False"                 
                    if isNotOnClosedList == "True":
                        # Set F and G values; add adjacent square to openList
                        onOpenList = "False"
                        for y in range(0, len(openList)):
                            if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                onOpenList = "True"
                        # If not already on open list, set G
                        if onOpenList == "False":
                            squares[row][column].setG(currentSquare.getG() + 10)
                        glabel = myfont.render(str(squares[row][column].getG()), 1, WHITE)
                        screen.blit(glabel, (squares[row][column].getX() + width/6, 
                                squares[row][column].getY() + height - height/3))
                        # F = G + H
                        squares[row][column].setF(squares[row][column].getG() + squares[row][column].getH())
                        flabel = myfont.render(str(squares[row][column].getF()), 1, WHITE)
                        screen.blit(flabel, (squares[row][column].getX() + width/6, 
                                squares[row][column].getY() + height/6))
                        isOnOpenList = "False"
                        for y in range(0, len(openList)):
                            if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                isOnOpenList = "True"
                        # If the square is not on the open list, add it; set parent
                        if isOnOpenList == "False":
                            openList.append(squares[row][column])
                            squares[row][column].setParent(currentSquare)
                        # If the square is on the open list, check to see if this new path is better using the G value
                        # Lower G => better path
                        elif isOnOpenList == "True":
                            oldG = squares[row][column].getG()
                            newG = currentSquare.getG() + 10
                            # Reset G value because this is a better path, change parent to current square, reset G and F values
                            if oldG > newG:
                                squares[row][column].setG(newG)
                                squares[row][column].setF(newG + squares[row][column].getH())
                                # Change parent to current square
                                squares[row][column].setParent(currentSquare)
def bottomRight():
    for row in range(numRows):
        for column in range(numCols):
            # Bottom right square
            if squares[row][column].getYCoordinate() == currentSquare.getYCoordinate()+1 and squares[row][column].getXCoordinate() == currentSquare.getXCoordinate()+1:
                # Check for obstacle in the way
                if squares[row][column-1].getSquareType() != "obstacle" and squares[row-1][column].getSquareType() != "obstacle":
                    # Check if this square is an obstacle
                    if squares[row][column].getSquareType() != "obstacle":
                        # Check that the square is not on the closed list already
                        isNotOnClosedList = "True"
                        for x in range(0, len(closedList)):
                            if closedList[x].getYCoordinate() == squares[row][column].getYCoordinate() and closedList[x].getXCoordinate() == squares[row][column].getXCoordinate():
                                isNotOnClosedList = "False"
                        if isNotOnClosedList == "True":
                            # Set F and G values; add adjacent square to openList
                            onOpenList = "False"
                            for y in range(0, len(openList)):
                                if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                    onOpenList = "True"
                                    # If not already on open list, set G
                            if onOpenList == "False":
                                squares[row][column].setG(currentSquare.getG() + 14)
                            glabel = myfont.render(str(squares[row][column].getG()), 1, WHITE)
                            screen.blit(glabel, (squares[row][column].getX() + width/6,
                                    squares[row][column].getY() + height - height/3))
                            # F = G + H
                            squares[row][column].setF(squares[row][column].getG() + squares[row][column].getH())
                            flabel = myfont.render(str(squares[row][column].getF()), 1, WHITE)
                            screen.blit(flabel, (squares[row][column].getX() + width/6, 
                                    squares[row][column].getY() + height/6))
                            isOnOpenList = "False"
                            for y in range(0, len(openList)):
                                if openList[y].getYCoordinate() == squares[row][column].getYCoordinate() and openList[y].getXCoordinate() == squares[row][column].getXCoordinate():
                                    isOnOpenList = "True"
                            # If the square is not on the open list, add it
                            if isOnOpenList == "False":
                                openList.append(squares[row][column])
                                squares[row][column].setParent(currentSquare)
                            # If the square is on the open list, check to see if this new path is better using the G value
                            # Lower G => better path
                            elif isOnOpenList == "True":
                                oldG = squares[row][column].getG()
                                newG = currentSquare.getG() + 14
                                # Reset G value because this is a better path, change parent to current square, reset G and F values
                                if oldG > newG:
                                    squares[row][column].setG(newG)
                                    squares[row][column].setF(newG + squares[row][column].getH())
                                    # Change parent to current square
                                    squares[row][column].setParent(currentSquare)

# Initalize some variables 
squares = [] # "2D array" of square objects
openList = [] # List of squares on the open list (squares that need to be checked)
closedList = [] # List of squares on the closed list
counter = 0 # Counter
fileName = "map1.txt" # Default loaded map
fps = 2 # Frames per second (speed of animation)

# This sets the width and height of each grid location
width  = 50
height = 50

# Default X, Y coordinates
startY = 2
startX = 2
goalY = 2
goalX = 6
startYCoordinate = startY
startXCoordinate = startX
goalYCoordinate = goalY
goalXCoordinate = goalX

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
RBLUE    = (  65, 105, 255)

# Read in command line arguments (if any)
for arg in sys.argv:
    if arg == "-X": # Start X
        startX = int(sys.argv[counter+1])
    elif arg == "-x": # Goal x
        goalX = int(sys.argv[counter+1])
    elif arg == "-Y": # Start Y
        startY = int(sys.argv[counter+1])
    elif arg == "-y": # Goal y
        goalY = int(sys.argv[counter+1])
    elif arg == "-f":
        fileName = sys.argv[counter+1]
    counter += 1

# Convert X grid coordinate to pixels
startX = startX * width + startX
startY = startY * height + startY
goalX = goalX * width + goalX
goalY = goalY * height + goalY

# Instantiate initial square, goal square
startSquare = Square(startY, startX, "start", GREEN)
goalSquare = Square(goalY, goalX, "goal", RED)
currentSquare = startSquare # set our current square to be the start square
indexInOpenList = 0
openList.append(currentSquare) # add the start square to our open list

print ()
print ("Loaded map file: ", fileName)
print ("Start coordinates: ", startSquare.getYCoordinate(),",", startSquare.getXCoordinate())
print ("Goal coordinates: ", goalSquare.getYCoordinate(),",", goalSquare.getXCoordinate())

# This sets the margin between each cell, default number of rows/cols
margin = 1
numRows = 5
numCols = 5

# Read in a file
f1 = open(fileName, 'r')
numberRows = 0 # calculated based on loaded file
numberCols = 0 

# Read in file and generate loaded map, preset square's h values
for line in f1:
    numberCols = 0 
    squares.append([]) # append a row
    for c in line:  
        if numberRows == startSquare.getYCoordinate() and numberCols == startSquare.getXCoordinate():
            squares[numberRows].append(startSquare)
            hVal = (abs(goalXCoordinate - startSquare.getXCoordinate()) + abs(goalYCoordinate - startSquare.getYCoordinate()))*10
            startSquare.setH(hVal)
            startSquare.setF(hVal)
            startSquare.setG(0)
        elif numberRows == goalSquare.getYCoordinate() and numberCols == goalSquare.getXCoordinate():
            squares[numberRows].append(goalSquare)
            goalSquare.setH(0)
        else:
            tempX = (width * numberCols) + (margin * numberCols)
            tempY = (height * numberRows) + (margin * numberRows)
            if c == 'o':
                square = Square(tempY, tempX, "obstacle", BLUE)
                hVal = hVal = (abs(goalXCoordinate - square.getXCoordinate()) + abs(goalYCoordinate - square.getYCoordinate()))*10
                square.setH(hVal)
                squares[numberRows].append(square)
            elif c == 'e':
                square = Square(tempY, tempX, "path", BLACK)
                hVal = (abs(goalXCoordinate - square.getXCoordinate()) + abs(goalYCoordinate - square.getYCoordinate()))*10
                square.setH(hVal)
                squares[numberRows].append(square)
        numberCols+=1
    numberRows+=1

numRows = numberRows
numCols = numberCols
maxXCoordinate = numberCols # set grid coordinate boundaries
maxYCoordinate = numberRows

screenWidth = width * numCols + margin * numCols + margin
screenHeight = height * numRows + margin * numRows + margin
 
f1.close() # close the file

# Initialize pygame
pygame.init()
  
# Set the height and width of the screen
size = [screenWidth, screenHeight]
screen = pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("A*")
 
# Loop until the user clicks the close button.
finished = False
userExit = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop ----------- #
while finished == False:
    # Handle quit / mouse click
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            userExit = True
            finished = True # Exit - user selected close
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                fps += 1
                print ("Increased frames per second:", fps)
            elif event.key == pygame.K_DOWN:
                if (fps > 1):
                    fps -= 1
                    print ("Decreased frames per second:", fps)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse - get mouse position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    # Set the screen background (grid line color)
    screen.fill(GREEN)
 
    # Draw the squares onto the grid
    for row in range(numRows):
        for column in range(numCols):
            # Draw all of our squares using our "array/list" of square objects
            pygame.draw.rect(screen, squares[row][column].getColor(), [squares[row][column].getX(), squares[row][column].getY(),
                                                                       width, height])
            myfont = pygame.font.SysFont("Arial", 10)
            hlabel = myfont.render(str(squares[row][column].getH()), 1, WHITE)

    # Begin A* Path Planning Algorithm
    minFVal = openList[0].getF() 
    currentSquare = openList[0]
    # Set current square to be the lowest F value square from the open list
    for x in range(0, len(openList)):
        if openList[x].getF() < minFVal:
            minFVal = openList[x].getF()
            currentSquare = openList[x]
    
    ###################################
    # Switch currentSquare to closed list
    ###################################
    openList.remove(currentSquare)
    closedList.append(currentSquare)
    
    for i in range(0, len(closedList)):
        if closedList[i].getXCoordinate() == goalSquare.getXCoordinate() and closedList[i].getYCoordinate() == goalSquare.getYCoordinate():
            finished = True
    
    
    ###################################
    # Determine type of square
    ###################################
    adjacentType = determineSquareType()
    
    ###################################
    # Adjacent squares logic
    ###################################
    if adjacentType == "top left":
        right()
        bottom()
        bottomRight()
    elif adjacentType == "top middle":
        left()
        right()
        bottomLeft()
        bottom()
        bottomRight()
    elif adjacentType == "top right":
        left()
        bottom()
        bottomLeft()
    elif adjacentType == "mid left":
        top()
        topRight()
        right()
        bottom()
        bottomRight()
    elif adjacentType == "mid middle":
        topLeft()
        top()
        topRight()
        left()
        right()
        bottomLeft()
        bottom()
        bottomRight()
    elif adjacentType == "mid right":
        topLeft()
        top()
        left()
        bottomLeft()
        bottom()
    elif adjacentType == "bottom left":
        top()
        topRight()
        right()
    elif adjacentType == "bottom middle":
        topLeft()
        top()
        topRight()
        left()
        right()
    elif adjacentType == "bottom right":
        topLeft()
        top()
        left()
    
    # Graphically mark squares that are on the open list
    for x in range (0, len(openList)):
        pygame.draw.rect(screen, RBLUE, [openList[x].getX(), openList[x].getY(),
                                                    width, height], 1)
        
        flabel = myfont.render(str(openList[x].getF()), 1, WHITE)
        glabel = myfont.render(str(openList[x].getG()), 1, WHITE)
        hlabel = myfont.render(str(openList[x].getH()), 1, WHITE)
        screen.blit(flabel, (openList[x].getX() + width/6,
                            openList[x].getY() + height/6))
        screen.blit(glabel, (openList[x].getX() + width/6, 
                            openList[x].getY() + height - height/3))
        screen.blit(hlabel, (openList[x].getX() + width - width/3,
                             openList[x].getY() + height - height/3))
        
    # Graphically mark squares that are on the closed list
    for x in range (0, len(closedList)):
        pygame.draw.rect(screen, RED, [closedList[x].getX(), closedList[x].getY(),
                                                    width, height], 1)
        flabel = myfont.render(str(closedList[x].getF()), 1, WHITE)
        glabel = myfont.render(str(closedList[x].getG()), 1, WHITE)
        hlabel = myfont.render(str(closedList[x].getH()), 1, WHITE)
        screen.blit(flabel, (closedList[x].getX() + width/6,
                            closedList[x].getY() + height/6))
        screen.blit(glabel, (closedList[x].getX() + width/6, 
                            closedList[x].getY() + height - height/3))
        screen.blit(hlabel, (closedList[x].getX() + width - width/3,
                             closedList[x].getY() + height - height/3))
         
    pygame.draw.rect(screen, WHITE, [currentSquare.getX(), currentSquare.getY(),
                                                width, height], 3)
    
    notFound = ""
    # Goal square not found
    if len(openList) == 0:
        finished = True
        notFound = "True"
    
    # Determine shortest path, trace route
    pathLength = 0
    if finished == True:
        pathLength = currentSquare.getF()
        if notFound != "True" and userExit == False:
            print ("Shortest path length: ", pathLength)
            while currentSquare.getXCoordinate() != startSquare.getXCoordinate() or currentSquare.getYCoordinate() != startSquare.getYCoordinate():
                p1 = currentSquare.getX() + 25, currentSquare.getY() + 25
                pygame.draw.circle(screen, GREEN, p1, 10)
                currentSquare = currentSquare.getParent()
        elif notFound == "True":
            print ("No path found!")
    
    # Limit to x frames per second
    clock.tick(fps)
    
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
    
done = False
while done == False:
    # Handle quit / mouse click
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            done = True # Exit - user selected close
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse - get mouse position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (width + margin)
            row = pos[1] // (height + margin)
            print("Click ", pos, "Grid coordinates: ", row, column)
# Exit pygame
pygame.quit()

