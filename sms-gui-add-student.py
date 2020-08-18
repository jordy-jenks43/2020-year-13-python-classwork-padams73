''' This program is the starter code for the student management system that we are building a GUI for
 It should be used for each new task.
 It has class definitions and generates all students and teachers, otherwise has no functionality.
 You will need to have this saved in the same folder as the teachers.csv and myRandomStudents.csv files.
 '''

from guizero import App, Text, TextBox, Combo, ListBox, PushButton


class Teacher:
    ''' Teachers have a name and a class they are attached to. '''

    def __init__(self, tname, tclass):
        ''' Set the attributes of the new teacher. '''

        self._tname = tname
        self._tclass = tclass
        # add new teacher to the list of all teachers
        teacher_list.append(self)

    def get_tname(self):
        ''' Return name of teacher. '''

        return self._tname

    def get_tclass(self):
        ''' Return the class. '''

        return self._tclass

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


def add_student():
    ''' Create new student using the data entered by the user. '''
    
    Student(name_text.value, age_text.value, phone_text.value, gender_combo.value, class_listbox.value)

    update_student_listbox()

def update_student_listbox():
    ''' Display all students in a listbox. '''
    
    students_list.clear()
    for student in student_list:
        students_list.append(student.get_name())
  
# Empty lists to store all teachers and students
teacher_list = []     
student_list = []

# Create some students to start with
Student("Jack", 16, "0273956577", "Male", ["GRA", "MAT", "ENG"])
Student("Jill", 15, "0271111111", "Female", ["MAT", "ART"])
Student("Matt", 17, "0217771117", "Male", ["MAT", "PHY", "ART"])

generate_teachers()
generate_students()

# create the application interface
app = App(title="Student management system", layout="grid")

# This is section where you add any GUI widgets

heading = Text(app, text="Add new student", grid=[0,0])
name_lbl = Text(app, text="Name", grid=[0,1])
name_text = TextBox(app, grid=[1,1])
age_lbl = Text(app, text="Age", grid=[0,2])
age_text = TextBox(app, grid=[1,2])
phone_lbl = Text(app, text="Phone", grid=[0,3])
phone_text = TextBox(app, grid=[1,3])
gender_lbl = Text(app, text="Gender", grid=[0,4])
gender_combo = Combo(app, options=["Male", "Female", "Other"], grid=[1,4])
class_lbl = Text(app, text="Classes", grid=[0,5], align="top")
class_listbox = ListBox(app, ["GRA", "BIO", "PHY", "MAT", "DTC", "ART", "ENG", "XYZ"], grid=[1,5], multiselect=True)
add_button = PushButton(app, text="Add student", grid=[0,6], command=add_student)

students_list = ListBox(app, grid=[2,1,1,6], align="top")

# Start the program
app.display()


