#----------------------------------------------------------------
#
# PASSCODE
#
# In this challenging exercise you will develop a non-trivial
# GUI program using Tkinter that comprises:
#
# 1) a ten digit keypad;
# 2) an 'OK' button; and
# 3) a text field.
#
# The program should allow numerical passcodes to be entered
# after which the OK button can be pressed.  If the passcode
# entered is a valid one then appropriate feedback should
# be provided, and similarly for invalid passcodes.
#
# The valid passcodes in this case should be your
# eight digit student numbers (with a leading zero).
#
# It is suggested that you develop this program in several
# steps:
#
# a) Write the 'back-end' function that recognises valid
#    passcodes.
# b) Develop a simple GUI 'front-end' for communicating
#    between the user and the back end, without worrying
#    about how the GUI widgets are laid out.
# c) Make the GUI look nice by laying out the widgets in
#    a natural format.
#
# Observation: To recognise the ten different digits we need
# ten separate functions attached to the buttons, meaning
# that some code will be duplicated 10 times.  Cleverer
# solutions which avoid this duplication are possible, but
# are too sophisticated for our current needs.  Brute
# force is acceptable here!
#

# Import the tkinter functions
from tkinter import *

# Create a window
passcode_window = Tk()

# Give the window a title
passcode_window.title('Passcode')


#### PUT YOUR SOLUTION HERE

# You will need to implement the following features:
#
# * A Text widget for providing feedback to the user
# * An 'OK' Button widget which, when pressed, calls a
#   function to see if a valid passcode has been entered
# * Ten Button widgets which, when pressed, call a
#   corresponding function to record the fact that the
#   button has been pushed
# * A global Python variable to keep track of the button
#   presses (digits entered) so far
# * Ten functions, one for each digit, which are called
#   when the corresponding button is pushed and add the
#   corresponding digit to the global variable
# * The function which is called when the 'OK' button
#   is presssed to check the global variable to see if a valid
#   passcode has been entered, to update the Text field
#   accordingly, and the reset the global variable ready
#   for the next passcode
#

passcode = ''
correct_code = "112233"

def add_digit(digit):
    global passcode
    passcode += str(digit)
    print(passcode)
    display.insert(END, "*")
    display.configure(background="white")

def buttonZero():
    add_digit(0)


def buttonOk():
    global passcode
    global correct_code

    if passcode == correct_code:
        display.configure(background="green")
    else:
        display.configure(background="red")
    
    passcode = ''
    display.delete(0.0,END)

counter = 1

for i in range(0,3):
    for j in range(0,3):
        button = Button(passcode_window, text=str(counter), command= lambda a = counter : (add_digit(a)))
        button.grid(row=i,column=j)
        counter += 1

zero_button = Button(passcode_window, text="0", command=buttonZero)
zero_button.grid(row=3,column=1)

ok_button = Button(passcode_window, text="OK", width=3, command=buttonOk)
ok_button.grid(row=4, column=0, columnspan=3)

display = Text(passcode_window, width=10, height=2)
display.grid(column=0, row=5, columnspan=3)

# Start the event loop
passcode_window.mainloop()