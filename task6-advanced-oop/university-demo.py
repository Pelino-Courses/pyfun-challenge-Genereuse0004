

from student import Student
from instructor import Instructor
from teaching_assistant import TeachingAssistant
from course import Course
from enrollment import Enrollment

def main():
 
    alice = Student("Alice", "alice@example.edu", "S001")
    bob = TeachingAssistant("Bob", "bob@example.edu", "S002", "CS")

    
    dr_smith = Instructor("Dr. Smith", "smith@example.edu", "Math")

    calculus = Course.create_lecture_course("MATH101", "Calculus I")
    lab = Course.create_lab_course("CS101L", "CS Lab")

    
    system = Enrollment()
    system.add_student(alice)
    system.add_student(bob)
    system.add_course(calculus)
    system.add_course(lab)

    
    system.enroll("S001", "MATH101")
    system.enroll("S002", "MATH101")
    system.enroll("S002", "CS101L")

    
    print(alice)
    print(list(alice))  # List of enrolled courses

    print(calculus)
    print("Students in calculus:", list(calculus))

    print(bob)
    print("Bob's courses:", list(bob))

    # Operator overloading: combine course rosters
    combined = calculus + lab
    print("Combined students:", combined)

if __name__ == "__main__":
    main()
