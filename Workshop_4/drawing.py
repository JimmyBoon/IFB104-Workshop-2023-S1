from turtle import *

setup(500, 500)
bgcolor('grey')


def draw(direction, position):
    '''This draws an arrow
    @param direction:
        float: Takes a direction as per a compass for where the arrow points
    @param position:
        tuple: x, y position where to draw the arrow
    '''
    setheading(90)
    goto(position[0], position[1])
    right(direction)
    color('yellow')
    pensize(4)
    forward(100)
    left(135)
    forward(50)
    left(135)
    forward(70)
    left(135)
    forward(50)

def writing(list_position, list_strings):
    if len(list_position) != len(list_strings):
        return
    
    for i in range(len(list_position)):

        penup()
        goto(list_position[i][0], list_position[i][1])
        pendown()
        write(list_strings[i])


# position = (-90,100)
# draw(140, position)
# penup()
# goto(100,100)
# pendown()
# write("This is me writing!", font=('Arial', 20, 'normal'))
positions = [(100,100), (0,0), (50,50)]
strings = ["Hello", "how are you", "good bye"]
writing(positions, strings)

hideturtle()

done()