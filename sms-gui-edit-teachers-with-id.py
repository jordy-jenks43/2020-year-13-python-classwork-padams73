''' This program is the starter code for the student management system that we are building a GUI for
 It should be used for each new task. 
 It has class definitions and generates all students and teachers, otherwise has no functionality.
 You will need to have this saved in the same folder as the teachers.csv and myRandomStudents.csv files.
 '''

from guizero import App, ListBox, Text


class Teacher:
    ''' Teachers have a name and a class they are attached to. '''
    
    def __init__(self, tname, tclass):
        ''' Set the attributes of the new teacher. '''
        
        self._tname = tname
        self._tclass = tclass
        
        if len(teacher_list)==0:
            self._tid = 1
        else:
            self._tid = teacher_list[-1].get_tid()+1
        
        # add new teacher to the list of all teachers
        teacher_list.append(self)

    def get_tname(self):
        ''' Return name of teacher. '''
        
        return self._tname
    
    def get_tclass(self):
        ''' Return the class. '''
        
        return self._tclass
    
    def get_tid(self):
        ''' Return the teacher ID. '''
        
        return self._tid
    
    def update(self, tname, tclass):
        ''' Update teacher name and class. '''
        
        self._tname = tname
        self._tclass = tclass

class Student:
    ''' The student class has a name, age, phone number, gender and a list of classes they are enrolled in. 
    All students are automatically set as enrolled when instantiated.
    Each student belongs to student_list. '''
    
    def __init__(self, name, age, phone, gender, classes):
        ''' This function sets the attributes of the new student.
        It sets every student to being enrolled by default. 
        It also adds the new student to student_list. '''
        
        self._name = name
        self._age = age
        self._phone = phone
        self._gender = gender
        self._classes = classes
        self._enrolled = True
        
        student_list.append(self)
        
    def get_name(self):
        ''' Return the name of the student. '''
        
        return self._name

    def get_age(self):
        ''' Return the age of the student. '''
        
        return self._age
    
    def get_phone(self):
        ''' Return the phone number of the student. '''
        
        return self._phone
    
    def get_gender(self):
        ''' Return the gender of the student. '''
        
        return self._gender
    
    def get_classes(self):
        ''' Return the list of classes the student is signed up for. '''
        
        return self._classes
    
    def get_enrolled(self):
        ''' Return whether or not a student is currently enrolled. '''
        
        return self._enrolled

def generate_teachers():
    ''' Import teachers from the teachers csv file. '''
    
    import csv
    # Notice the encoding setting. This avoids the byte order mark (BOM)
    # appearing. This looks like: ﻿
    with open('teachers.csv', encoding="utf-8-sig", newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            Teacher(line[0], line[1])

def generate_students():
    ''' Import students from the myRandomStudents csv file. '''
    
    import csv
    with open('myRandomStudents.csv', newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for line in filereader:
            classes=[]
            i=4
            while i in range(4, 9):
                classes.append(line[i])
                i+=1
            Student(line[0], int(line[1]), line[2],line[3], classes)

def display_details():
    ''' Display teacher name and class in textboxes. '''
    
    for teacher in teacher_list:
        if teacher.get_tname() == teacher_listbox.value:
            name_textbox.value = teacher.get_tname()
            class_textbox.value = teacher.get_tclass()
 
def update_details():
    ''' Update details of selected teacher. '''
    
    for teacher in teacher_list:
        if teacher.get_tname() == teacher_listbox.value:
            teacher.update(name_textbox.value, class_textbox.value)
    update_listbox()
    name_textbox.clear()
    class_textbox.clear()

def update_listbox():
    ''' Clear and update the listbox. '''
    
    teacher_listbox.clear()
    for teacher in teacher_list:
        teacher_listbox.append(teacher.get_tname()) 

      
  
# Empty lists to store all teachers and students
teacher_list = []     
student_list = []

# Create some students to start with
Student("Jack", 16, "0273956577", "Male", ["GRA", "MAT", "ENG"])
Student("Jill", 15, "0271111111", "Female", ["MAT", "ART", "XYZ"])
Student("Matt", 17, "0217771117", "Male", ["MAT", "PHY", "ART"])

generate_teachers()
generate_students()

# create the application interface
app = App(title="Student management system")

from guizero import App, ListBox, TextBox, PushButton, warn

# ListBox contains names of all teachers
# Set up list of names and ids of teachers
list_content = []
for teacher in teacher_list:
    list_content.append([teacher.get_tname(), teacher.get_tid()])
teacher_listbox = ListBox(app, items=[], command=display_details)

name_textbox = TextBox(app)
class_textbox = TextBox(app)

update_button = PushButton(app, text="Update details", command=update_details)



# Start the program
app.display()


