class Student:
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
        self.courses = []

    def enroll(self, course: 'Course'):
        if course not in self.courses:
            self.courses.append(course)

    def __repr__(self):
        return f"Student(name={self.name!r}, email={self.email!r})"
