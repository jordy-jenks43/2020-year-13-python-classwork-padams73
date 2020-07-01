''' This program demonstrates how to use grid to design the GUI. '''

# first, we need to import the guizero library
from guizero import App, Text

# This time when we create the window we are setting the layout to grid, where each widget needs to be placed in a specific location using grid coordinates
app = App(title="This is our window", layout="grid")

# To create a textbox we define a variable and assign it to the Text class.
# There are multiple parameters to set. 
# The first is location, which will app in this case as the text box is located directly in the main app window.
# The second is the text to display
# In this example, because we are using grid layout we need to specify the location in the app window
heading = Text(app, text="This app demonstrates grid layout", grid=[0,0])
# here we set the colour of the text to red, using RGB
heading.text_color = (255, 0, 0)

another_label = Text(app, text="This is the second row, second column", grid=[1,1])

third_label = Text(app, text="This is the third row, first column\n [0,2]", grid=[0,2])
# This is the last line, which is needed to start the GUI running
app.display()