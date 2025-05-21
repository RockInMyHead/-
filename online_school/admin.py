from .school import School


def admin_panel():
    school = School("Онлайн Школа")
    actions = {
        "1": "Добавить курс",
        "2": "Добавить контрольную работу",
        "3": "Список курсов",
        "4": "Список контрольных работ",
        "0": "Выход",
    }
    while True:
        print("\nПанель администратора:")
        for k, v in actions.items():
            print(f"{k}. {v}")
        choice = input("Выберите действие: ").strip()
        if choice == "1":
            title = input("Название курса: ").strip()
            teacher = input("Преподаватель: ").strip()
            try:
                school.add_course(title, teacher)
                print("Курс добавлен")
            except ValueError as e:
                print(e)
        elif choice == "2":
            course_title = input("Курс: ").strip()
            test_title = input("Название контрольной: ").strip()
            try:
                school.add_test(course_title, test_title)
                print("Контрольная работа добавлена")
            except ValueError as e:
                print(e)
        elif choice == "3":
            for c in school.list_courses():
                print(f"- {c.title} ({c.teacher})")
        elif choice == "4":
            for t in school.list_tests():
                print(f"- {t.title} (курс {t.course.title})")
        elif choice == "0":
            break
        else:
            print("Неизвестная команда")


if __name__ == "__main__":
    admin_panel()
