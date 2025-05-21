from .school import School


def demo():
    school = School("Онлайн Школа")
    school.add_student("Иван", "ivan@example.com")
    school.add_student("Мария", "maria@example.com")

    school.add_course("Математика", "Петров П.П.")
    school.add_course("Физика", "Иванов И.И.")

    school.enroll_student("Иван", "Математика")
    school.enroll_student("Мария", "Физика")

    for course in school.list_courses():
        print(f"Курс: {course.title}, преподаватель: {course.teacher}")
        for student in course.students:
            print(f"  - {student.name} <{student.email}>")


if __name__ == "__main__":
    demo()
