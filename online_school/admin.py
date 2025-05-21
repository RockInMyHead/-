from .school import School


def main():
    school = School("Онлайн Школа")

    while True:
        print("1. Add course")
        print("2. Add test")
        print("3. List courses")
        print("4. List tests")
        print("5. Quit")
        choice = input("Select option: ")
        if choice == "1":
            title = input("Course title: ")
            teacher = input("Teacher: ")
            try:
                school.add_course(title, teacher)
            except ValueError as e:
                print(e)
        elif choice == "2":
            course_title = input("Course title: ")
            test_title = input("Test title: ")
            try:
                school.add_test(test_title, course_title)
            except ValueError as e:
                print(e)
        elif choice == "3":
            for c in school.list_courses():
                print(f"- {c.title} ({c.teacher})")
        elif choice == "4":
            for t in school.list_tests():
                print(f"- {t.title} ({t.course.title})")
        elif choice == "5":
            break
        else:
            print("Unknown option")


if __name__ == "__main__":
    main()
