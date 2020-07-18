''' This program demonstrates how to add a ButtonGroup to the GUI. '''

# first, we need to import the guizero library
from guizero import App, ButtonGroup, PushButton, Text

def check_selection():
    ''' Display hidden value of item selected. '''
    
    label.value = class_choice.value

# We create an instance of the App class (which is just the a window), giving it a title
app = App(title="Demonstrating ButtonGroup")

class_choice = ButtonGroup(app, options=[["Graphics", "GRA"], ["Mathematics", "MTH"], ["Digital Technologies", "INT"]])
button = PushButton(app, text="Check selection", command=check_selection)
label = Text(app)


# This is the last line, which is needed to start the GUI running
app.display()