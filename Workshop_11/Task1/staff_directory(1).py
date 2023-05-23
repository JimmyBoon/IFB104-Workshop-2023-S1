#--------------------------------------------------------------------#
#
# Staff Directory Front-End
#
# This is the front-end of the staff directory application. It
# creates a Graphical User Interface which can be used with any
# of the back-end functions.
#
# To complete this exercise you need to work with your teammates
# to decide who will implement the front-end GUI and who will
# implement the back-end look-up function. You need to agree on
# the signature of this function so that both teams can work
# independently, i.e., what parameter(s) does the function accept
# and what format does it return the search results in?
#
# Below is some skeletal code to help you get started on the
# front-end, but feel free to design whatever GUI you want to
# do the job.  
#

# Import the Tkinter functions
from tkinter import *

# Import the back-end function developed by the other team
from backend_function import search_by_db, add_employee_rating


#--------------------------------------------------------------------#
# Define a function here to serve as the "command" when the user
# initiates a search.  It should:
#
# 1) get the employee name entered by the user;
# 2) call the back-end function to get the search results; and
# 3) display the results in the GUI.
#

def searchEntry(Label, entrytext = None):
    if entrytext == None:
        return
    
    ##Put return data here to replace the text in the label
    Label['text'] = entrytext
    for emp_no, birth_date, first_name, last_name, gender, hire_date in search_by_db(entrytext):
        Label['state'] = 'normal'
        Label.insert('1.0',f"{emp_no}: {first_name}, {last_name}, {birth_date}\n")
        Label['state'] = 'disabled'
    #add_employee_rating(1000, entrytext)
    
        
#----------------------------------------------------------------#
# The GUI front end
#

# Create a window
staff_window = Tk()

# Give the window a title
staff_window.title('Staff Directory')

# Create a Text widget to display the results
displayFrame = Frame(staff_window, width=250, height=250, background="lightgrey", highlightbackground="grey", highlightthickness=1)
displayFrame.pack(padx=5, pady=5)
displayFrame.pack_propagate(0)
displayLabel = Text(displayFrame, font=("calibre 10"), background="lightgrey")
displayLabel.pack(padx=5, pady=5, anchor=W)
displayLabel['state'] = 'disabled'
# Create a text Entry widget for entering the employee name
displayEntry = Entry(staff_window, background="lightgrey")
displayEntry.pack(pady=5)

# Create a Button widget to start the search
displayButton = Button(staff_window, text="Enter", background="lightgrey", command=lambda:searchEntry(displayLabel, displayEntry.get()))
displayButton.pack(pady=5)

# Optional: Create any other widgets you want to make
# the GUI look nice, such as Labels for instructions or
# to display an image

# Start the event loop
staff_window.mainloop()

#
#--------------------------------------------------------------------#

