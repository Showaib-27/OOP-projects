# """
# Define a class Student with the following instance attributes:
# - student_id: Unique identifier for the student.
# - name: Full name of the student.
# - department: The department of the student.
# - is_enrolled: A boolean indicating if the student is currently enrolled.
# """
class Student:
    def __init__(self, student_id, name, dept):
        self.__student_id = student_id
        self.__name = name
        self.__dept = dept
        self.__is_enrolled = False
        StudentDatabase.add_student(self)

# """
# # Add a method enroll_student() in the Student class that checks 
# # if the student is not already enrolled.
# # If not, change is_enrolled to True.
# """
    def enroll_student(self):
        if not self.__is_enrolled:
            self.__is_enrolled = True
            print(f"Student {self.__name} (ID: {self.__student_id}) has been enrolled")
        else:
            print(f"Student {self.__name} (ID: {self.__student_id}) already enrolled")

# """
# Add a method drop_student() in the Student class
# that changes is_enrolled to False to indicate 
# the student has dropped out.
# """
    def drop_student(self):
        if self.__is_enrolled:
            self.__is_enrolled = False
            print(f"Student {self.__name} (ID:{self.__student_id}) has been dropped out")
        else:
            print(f"Student {self.__name} (ID:{self.__student_id}) is not enrolled")

# Add a method view_student_info() in the Student class to display the details of 
# the student including student_id, name, department, and enrollment status.

    def view_student_info(self):
        
        enrollment = "Enrolled" if self.__is_enrolled else "Not enrolled"
        print(f"ID:{self.__student_id} Name:{self.__name} Department:{self.__dept} status:{enrollment}")


    def check_student_id(self):
        return self.__student_id
    
# Define a class named StudentDatabase with one
# class attribute named student_list. Initially, 
# it should be an empty list. 
# Create a class method add_student() to insert 
# an object of the Student class into student_list.    

class StudentDatabase:
    student_list = []

    @classmethod
    def add_student(cls, student):
        if isinstance(student, Student):
            cls.student_list.append(student)
        else:
            print("Invalid")
    
    @classmethod
    def find_student(cls, student_id):
        for student in cls.student_list:
            if student.check_student_id() == student_id:
                return student
        return None
    @classmethod
    def view_all_student(cls):
        if cls.student_list:
            for student in cls.student_list:
                student.view_student_info()
        else:
            print("No student in database")

# Create a menu-driven system with the following options:
# 1. View All Students
# 2. Enroll Student
# 3. Drop Student
# 4. Exit
# Handle the user’s choice using input prompts

def menu():
    while True:
        print("\nMenu")
        print("1. View All Student")
        print("2. Enroll Student")
        print("3. Drop Student")
        print("4. Exit")

        choice = input("Enter ur choice(1-4):")
        if choice == "1":
            StudentDatabase.view_all_student()
        elif choice =="2":
            student_id = int(input("Enter Student to Enroll: "))
            student = StudentDatabase.find_student(student_id)
            if student:
                student.enroll_student()
            else:
                print("Invalid Student ID")
        elif choice == "3":
            student_id = int(input("Enter Student to DropOut: "))
            student = StudentDatabase.find_student(student_id)
            if student:
                student.drop_student()
            else:
                print("Invalid Student ID")
        elif choice == "4":
            print("Exiting")
            break
        else:
            print("Invalid choice, Enter Valid choice")

Student(101, "Showaib", "EEE")
Student(102, "Ashif", "CSE")


menu()    