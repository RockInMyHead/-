from .school import School


def main():
    school = School("Онлайн Школа")
    while True:
        print("\nАдмин панель")
        print("1. Добавить курс")
        print("2. Добавить контрольную работу")
        print("3. Список курсов")
        print("4. Список контрольных работ")
        print("5. Выход")
        choice = input("Выберите пункт: ").strip()

        if choice == "1":
            title = input("Название курса: ").strip()
            teacher = input("Преподаватель: ").strip()
            try:
                school.add_course(title, teacher)
                print("Курс добавлен")
            except ValueError as e:
                print(e)
        elif choice == "2":
            course_title = input("Для какого курса: ").strip()
            test_title = input("Название контрольной: ").strip()
            try:
                school.add_test(course_title, test_title)
                print("Контрольная добавлена")
            except ValueError as e:
                print(e)
        elif choice == "3":
            for course in school.list_courses():
                print(f"- {course.title} ({course.teacher})")
        elif choice == "4":
            for test in school.list_tests():
                print(f"- {test.title} (курс: {test.course.title})")
        elif choice == "5":
            break
        else:
            print("Неизвестный пункт меню")


if __name__ == "__main__":
    main()
