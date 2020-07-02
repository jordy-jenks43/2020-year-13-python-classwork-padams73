''' This program demonstrates how to add a text box to the GUI. '''

# first, we need to import the guizero library
from guizero import App, TextBox, PushButton

def print_text():
    ''' Print the contents of the text_entry TextBox. '''
    
    print(text_entry.value)


# We create an instance of the App class (which is just the a window), giving it a title
app = App(title="This is our window")

# To create a textbox we define a variable and assign it to the Text class.

text_entry = TextBox(app)


# A button below the text_entry widget will call the print_text() function, printing out the content of the TextBox
print_button = PushButton(app, text="Print", command=print_text)


# This is the last line, which is needed to start the GUI running
app.display()