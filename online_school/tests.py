class Test:
    def __init__(self, title: str, course: 'Course'):
        self.title = title
        self.course = course

    def __repr__(self):
        return f"Test(title={self.title!r}, course={self.course.title!r})"

