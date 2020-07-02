''' Demo how to use a textbox and call functions using
a PushButton. Also how to update a Text label. '''

from guizero import App, TextBox, Text, PushButton

def print_stuff():
    ''' Display the contents of the text_entry TextBox. '''
    
    text.value = text_entry.value
    
app = App(title="PushButton and TextBox demo")

# create a textBox called text_entry
text_entry = TextBox(app, width="fill", multiline=True,height=2)

# Create a button to print out what the user entered
print_button = PushButton(app, text="Push me", command=print_stuff)
print_button.bg = (200,0,0)
print_button.text_color="white"
print_button.text_size=30

# Label to display content
text = Text(app)

app.display()