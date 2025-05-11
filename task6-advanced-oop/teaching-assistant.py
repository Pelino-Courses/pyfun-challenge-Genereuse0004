

from student import Student
from instructor import Instructor


class TeachingAssistant(Student, Instructor):
   

    def __init__(self, name: str, email: str, student_id: str, department: str):
        Student.__init__(self, name, email, student_id)
        Instructor.__init__(self, name, email, department)

    def get_role(self) -> str:
        return "Teaching Assistant"
