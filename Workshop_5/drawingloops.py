from turtle import *
from random import randint

setup(1000,1000)

def createPoint(posMax):
    
    myColours = ["Blue", "Yellow", "Black", "Green", "Pink"]
    colourPicker = randint(0, 20)

    if colourPicker < len(myColours):
        return myColours[colourPicker]

    xpos = randint(-posMax, posMax)
    ypos = randint(-posMax, posMax)
    dotsize = randint(1, 20)
    coord = [xpos, ypos, dotsize]
    return coord
    
def buildInstructions(colour, number):
    instructions = []
    instructions.append(colour)

    for _ in range(0, number):
        instructions.append(createPoint(400))
    print(instructions)
    return instructions

def drawTheArt(startColour, bigColour, numDots):
    for instruct in buildInstructions(startColour, numDots):

        if type(instruct) == str:
            colour = instruct
            continue
        
        if instruct[1] > 0:
            pendown()
        else:
            penup()

        if instruct[2] > 18:
            pencolor(bigColour)
        else:
            pencolor(colour)
        

        pensize(instruct[2])
        goto(instruct[0], instruct[1])
        dot()

drawTheArt("Purple", "Blue", 50)


done()
