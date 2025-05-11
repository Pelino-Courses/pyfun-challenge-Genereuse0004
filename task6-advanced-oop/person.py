

from abc import ABC, abstractmethod


class EmailDescriptor:
    
    def __get__(self, instance, owner):
        return instance.__dict__.get('_email')

    def __set__(self, instance, value):
        if "@" not in value or "." not in value:
            raise ValueError("Invalid email address.")
        instance.__dict__['_email'] = value


class Person(ABC):
    
    
    email = EmailDescriptor()

    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email

    @abstractmethod
    def get_role(self) -> str:
        
        pass

    def __str__(self) -> str:
        return f"{self.get_role()}: {self.name} ({self.email})"
