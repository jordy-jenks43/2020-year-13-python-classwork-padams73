''' This program is a student management system, allowing users to add student records and run reports. '''

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
    
    name = input("Name to search for: ")
    for student in student_list:
        # using .lower() to ensure we get matches with different cases
        if name.lower() in student.get_name().lower():
            show_details(student)
 
  
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
    

     
student_list = []

# Create some students to start with
Student("Jack", 16, "0273956577", "Male", ["GRA", "MAT", "ENG"])
Student("Jill", 15, "0271111111", "Female", ["MAT", "ART"])
Student("Matt", 17, "0217771117", "Male", ["MAT", "PHY", "ART"])

generate_students()

run_program = True
while run_program == True:
    print("Main Menu\n-----------")
    print("1. Search")
    print("2. Add student")
    print("3. Class list")
    print("4. Quit")
    selection = int(input("Selection:"))
    if selection == 1:
        search()
    elif selection == 2:
        add_student()
    elif selection == 3:
        class_list()
    elif selection == 4:
        run_program = False
    else:
        print("Enter a number from 1-4")


