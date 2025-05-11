# student.py

from person import Person
from typing import List, Iterator


class Student(Person):
    

    def __init__(self, name: str, email: str, student_id: str):
        super().__init__(name, email)
        self.student_id = student_id
        self._courses: List[str] = []

    def enroll_in_course(self, course_code: str):
        if course_code not in self._courses:
            self._courses.append(course_code)

    def __iter__(self) -> Iterator[str]:
        return iter(self._courses)

    def get_role(self) -> str:
        return "Student"
