''' This program demonstrates how to add a text label to the GUI. '''

# first, we need to import the guizero library
from guizero import App, Text

# We create an instance of the App class (which is just the a window), giving it a title
app = App(title="This is our window")

# To create a text label we define a variable and assign it to the Text class.
# There are multiple parameters to set. 
# The first is location, which will app in this case as the text label is located directly in the main app window.
# The second is the text to display
heading = Text(app, text="Welcome to my first app")
# here we set the colour of the text to red, using RGB
heading.text_color = (255, 0, 0)


# This is the last line, which is needed to start the GUI running
app.display()