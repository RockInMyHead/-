from .students import Student
from .courses import Course



class Test:
    """Represents a control work linked to a course."""

    def __init__(self, title: str, course: Course):
        self.title = title
        self.course = course

    def __repr__(self):
        return f"Test(title={self.title!r}, course={self.course.title!r})"


class School:
    def __init__(self, name: str):
        self.name = name
        self.students = {}
        self.courses = {}
        self.tests = []

    def add_student(self, name: str, email: str) -> Student:
        if name in self.students:
            raise ValueError(f"Student {name} already exists")
        student = Student(name, email)
        self.students[name] = student
        return student

    def add_course(self, title: str, teacher: str) -> Course:
        if title in self.courses:
            raise ValueError(f"Course {title} already exists")
        course = Course(title, teacher)
        self.courses[title] = course
        return course


    def add_test(self, title: str, course_title: str) -> Test:
        course = self.courses.get(course_title)
        if not course:
            raise ValueError(f"Unknown course: {course_title}")
        test = Test(title, course)
        self.tests.append(test)
        return test

    def enroll_student(self, student_name: str, course_title: str):
        student = self.students.get(student_name)
        if not student:
            raise ValueError(f"Unknown student: {student_name}")
        course = self.courses.get(course_title)
        if not course:
            raise ValueError(f"Unknown course: {course_title}")
        course.add_student(student)

    def list_students(self):
        return list(self.students.values())

    def list_courses(self):
        return list(self.courses.values())


    def list_tests(self):
        return list(self.tests)

