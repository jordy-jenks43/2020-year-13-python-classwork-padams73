''' This program demonstrates how to create a GUI window using guizero. '''

# first, we need to import the guizero library
from guizero import App

# We create an instance of the App class (which is just the a window)
# We can set a title and background colour (using RGB codes)
app = App(title="This is a red window", bg=(255, 0, 0))



# This is the last line, which is needed to start the GUI running
app.display()