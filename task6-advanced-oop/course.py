

from typing import List, Iterator


class Course:
    

    def __init__(self, code: str, name: str, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be a positive number.")
        self.code = code
        self.name = name
        self.capacity = capacity
        self.students: List[str] = []

    def enroll(self, student_id: str):
        if len(self.students) >= self.capacity:
            raise OverflowError(f"Course {self.code} is full.")
        if student_id not in self.students:
            self.students.append(student_id)

    def __iter__(self) -> Iterator[str]:
        return iter(self.students)

    def __add__(self, other: 'Course') -> List[str]:
        """Combine student lists from two courses."""
        return list(set(self.students + other.students))

    def __contains__(self, student_id: str) -> bool:
        return student_id in self.students

    def __str__(self) -> str:
        return f"{self.code} - {self.name} ({len(self.students)}/{self.capacity})"

    @classmethod
    def create_lab_course(cls, code: str, name: str) -> 'Course':
        return cls(code, name, capacity=15)

    @classmethod
    def create_lecture_course(cls, code: str, name: str) -> 'Course':
        return cls(code, name, capacity=100)
