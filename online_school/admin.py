from .school import School


def main():
    school = School("Администрирование")
    while True:
        print("1. Добавить курс")
        print("2. Добавить контрольную работу")
        print("3. Список курсов")
        print("4. Список контрольных работ")
        print("5. Выход")
        choice = input("> ")
        if choice == "1":
            title = input("Название курса: ")
            teacher = input("Преподаватель: ")
            try:
                school.add_course(title, teacher)
                print("Курс добавлен")
            except ValueError as e:
                print(e)
        elif choice == "2":
            title = input("Название контрольной: ")
            course_title = input("Курс: ")
            try:
                school.add_test(title, course_title)
                print("Контрольная добавлена")
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
            print("Неизвестная команда")


if __name__ == "__main__":
    main()
