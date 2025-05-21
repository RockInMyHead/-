class Course:
    def __init__(self, title: str, teacher: str):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student: 'Student'):
        if student not in self.students:
            self.students.append(student)
            student.enroll(self)

    def __repr__(self):
        return f"Course(title={self.title!r}, teacher={self.teacher!r})"
