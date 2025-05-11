# instructor.py

from person import Person
from typing import List


class Instructor(Person):
    

    def __init__(self, name: str, email: str, department: str):
        super().__init__(name, email)
        self.department = department
        self.courses_taught: List[str] = []

    def assign_course(self, course_code: str):
        if course_code not in self.courses_taught:
            self.courses_taught.append(course_code)

    def get_role(self) -> str:
        return "Instructor"
