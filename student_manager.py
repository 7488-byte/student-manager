####STUDENT MANAGER 
class Student():
    def __init__(self,name,id,marks,courses):
        self.name = name 
        self.id = id
        self.marks = marks
        self.courses = courses

    def show_info(self):
        return f"NAME:{self.name.title()}\nID:{self.id}\nMarks:{self.marks}\nCourses:{self.courses}"
    
students = {}
n = int(input("no of students : "))
for i in range(n):
    student_name = input("enter student name : ")
    student_id = input("enter student id : ")
    student_marks = input("enter marks(separated by commas): ")
    student_courses = input("enter courses : ")
    marks = [int(m.strip()) for m in student_marks.split(",")]
    courses = [c.strip() for c in student_courses.split(",")]
    student = Student(student_name,student_id,marks,courses)
    students[student_id]=student

for student in students.values():
    print(student.show_info())
    print()

######## FILTER STUDENT BY MARKS #######
class Student():
    def __init__(self,name,id,marks,courses):
        self.name = name 
        self.id = id
        self.marks = marks
        self.courses = courses

    def show_info(self):
        return f"NAME:{self.name.title()}\nID:{self.id}\nMarks:{self.marks}\nCourses:{self.courses}"
    
students = {}
n = int(input("no of students : "))
for i in range(n):
    student_name = input("enter student name : ")
    student_id = input("enter student id : ")
    student_marks = int(input("enter mark: "))
    student_courses = input("enter courses : ")
    courses = [c.strip() for c in student_courses.split(",")]
    student = Student(student_name,student_id,student_marks,courses)
    students[student_id]=student

Threshold_marks = int(input("Enter minimum marks:"))
print(f"-----students above {Threshold_marks}-------- ")
for student in students.values():
    if student.marks >= Threshold_marks:
        print(student.show_info())
        print()

########## NEXT STEP - UPDATE MARKS OF A STUDENT 

class Student():
    def __init__(self,name,id,marks,courses):
        self.name = name 
        self.id = id
        self.marks = marks
        self.courses = courses

    def show_info(self):
        return f"NAME:{self.name.title()}\nID:{self.id}\nMarks:{self.marks}\nCourses:{self.courses}"
    
    def update_marks(self,new_marks):
        self.marks = new_marks

students = {}
n = int(input("no of students : "))
for i in range(n):
    student_name = input("enter student name : ")
    student_id = input("enter student id : ")
    student_marks = int(input("enter mark: "))
    student_courses = input("enter courses : ")
    courses = [c.strip() for c in student_courses.split(",")]
    student = Student(student_name,student_id,student_marks,courses)
    students[student_id]=student

Threshold_marks = int(input("Enter minimum marks:"))
print(f"-----students above {Threshold_marks}-------- ")
for student in students.values():
    if student.marks >= Threshold_marks:
        print(student.show_info())
        print()

choice = input("Do you want to update marks for any student?(yes/no): ")
if choice=='yes':
    update_id = input("Enter student id which need updation: ")
    if update_id in students:
        new_marks = int(input("enter new marks : "))
        students[update_id].update_marks(new_marks)
        print("Marks updated successfully!")
        print("\nUpdated Info:")
        print(students[update_id].show_info())
    else:
        print("No student found with that ID.")

