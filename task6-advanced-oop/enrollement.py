

from typing import Dict
from student import Student
from course import Course


class Enrollment:
    

    def __init__(self):
        self.students: Dict[str, Student] = {}
        self.courses: Dict[str, Course] = {}

    def add_student(self, student: Student):
        if student.student_id in self.students:
            raise ValueError("Student already exists.")
        self.students[student.student_id] = student

    def add_course(self, course: Course):
        if course.code in self.courses:
            raise ValueError("Course already exists.")
        self.courses[course.code] = course

    def enroll(self, student_id: str, course_code: str):
        if student_id not in self.students:
            raise LookupError("Student not found.")
        if course_code not in self.courses:
            raise LookupError("Course not found.")

        course = self.courses[course_code]
        student = self.students[student_id]

        course.enroll(student_id)
        student.enroll_in_course(course_code)
