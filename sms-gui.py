''' This program is a student management system, allowing users to add student records and run reports. '''

import generate
from guizero import App, Text, PushButton, TextBox, ListBox

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

def class_count():
    ''' Count how many students in the class the user enters. '''
    
    class_code = input("Enter class code: ")
    total = 0
    for student in student_list:
        if class_code.upper() in student.get_classes():
            total += 1
    print("Total students:", total)

def class_list():
    ''' Get list of students in selected class. '''
    
    class_code = input("Enter class code: ")
    # get the name of the teacher who teaches this class
    for teacher in teacher_list:
        if teacher.get_tclass() == class_code:
            print("Teacher: {}".format(teacher.get_tname()))
    # display names of all students in class, as well as a count
    total = 0
    for student in student_list:
        if class_code.upper() in student.get_classes():
            print(student.get_name())
            total += 1
    print("Total students:", total)    

def show_all():
    ''' This function shows the names of all students. '''
    
    for student in student_list:
        print(student.get_name())
        
def search():
    ''' Display details of student. '''
    
    # Empty the search_list listbox
    search_list.clear()

    for student in student_list:
        # using .lower() to ensure we get matches with different cases
        if search_box.value.lower() in student.get_name().lower():
            
            search_list.append(student.get_name())

 
  
def show_details(student_to_show):
    ''' Display details of student. '''
    
    print("####################")
    print(student_to_show.get_name())
    print("--------------------")
    print("Age:", student_to_show.get_age())
    print("Phone:", student_to_show.get_phone())
    print("")

def add_student():
    ''' Add new student record. '''
    
    print("Enter student details")
    name = input("Name: ")
    # ask for student age. Use while loop to ensure we get an integer
    ask_age = True
    while ask_age == True:
        try:
            age = int(input("Age: "))
            ask_age = False
        except:
            print("Invalid input. Please enter an integer.")

    phone = input("Phone: ")
    gender = input("Gender: ")
    new_classes = []
    ask_class = True
    while ask_class == True:
        new_class = input("Class code (end to finish): ")
        if new_class.lower() == "end":
            ask_class = False
        elif new_class == "":
            print("Please enter a class code")
        else:
            new_classes.append(new_class)
    # instantiate the new student
    Student(name, age, phone, gender, new_classes)

def print_tname(t):
    ''' Print the name of the selected teacher. '''
    
    print(t.get_tname())




    
# Empty lists to store all teachers and students
teacher_list = []     
student_list = []

# Create some students to start with
Student("Jack", 16, "0273956577", "Male", ["GRA", "MAT", "ENG"])
Student("Jill", 15, "0271111111", "Female", ["MAT", "ART"])
Student("Matt", 17, "0217771117", "Male", ["MAT", "PHY", "ART"])

generate_teachers()
generate_students()

# We create an instance of the App class (which is just the a window), giving it a title
app = App(title="Student Management System", layout="grid")


# In this section we have a text entry field where the user can type the name of the student to search for
# When the Search button is pressed, a search function is called which then displays the names for all matching records in a list
search_box = TextBox(app, width="fill", grid=[0,0])
search_button = PushButton(app, text="Search", grid=[0,1], command=search)



# Results label
search_results = Text(app, grid=[1,2], align="left")

def update_search_results():
    ''' Display details of selected student. '''
    
    # set the initial value of the search_results text label

    search_results.clear()
    search_results.value = "Results\n"
    search_results.append(search_list.value)


# Listbox for results of search
search_list = ListBox(app, grid=[0,2])
search_list.when_left_button_pressed = update_search_results



# This is the last line, which is needed to start the GUI running
app.display()



''' Playing around with creating dynamic buttons
# Loop through teacher list and display names in text boxes
for teacher in teacher_list:
    #teacher_name = Text(app, text=teacher.get_tname())
    # Each button has the teacher's name as the label. It calls the print_tname() function and sends the teacher object to that function
    teacher_button = PushButton(app, text=teacher.get_tname()).update_command(print_tname, [teacher])

'''