from .school import School


def main():
    school = School("Админ школа")
    menu = (
        "1. Добавить курс",
        "2. Добавить контрольную работу",
        "3. Список курсов",
        "4. Список контрольных",
        "5. Выход",
    )
    while True:
        for item in menu:
            print(item)
        choice = input("Выберите пункт: ").strip()
        if choice == '1':
            title = input("Название курса: ")
            teacher = input("Преподаватель: ")
            try:
                school.add_course(title, teacher)
            except ValueError as e:
                print(e)
        elif choice == '2':
            title = input("Название контрольной: ")
            course = input("Курс: ")
            try:
                school.add_test(title, course)
            except ValueError as e:
                print(e)
        elif choice == '3':
            for c in school.list_courses():
                print(f"- {c.title} ({c.teacher})")
        elif choice == '4':
            for t in school.list_tests():
                print(f"- {t.title} -> {t.course.title}")
        elif choice == '5':
            break
        else:
            print("Неверный пункт")
        print()


if __name__ == "__main__":
    main()

