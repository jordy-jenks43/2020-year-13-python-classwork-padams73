''' Demonstrate how guizero works. '''

# import the widgets we need from guizero
from guizero import App, Text

# Create the main window
app = App(layout="grid", title="My first guizero app", bg=(200,200,200), height=400, width=600)

# Create a text label
# the first parameter is the location of the widget
header = Text(app, grid=[0,0], text="Welcome to my program", font="Calibri", size=30, color="red")

label = Text(app, grid=[1,0], text="Hi how are you")

# Starts the program by displaying the main window
app.display()
