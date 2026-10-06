"""main.py — точка входа приложения «Заметки».

Запуск:  python main.py
Меню:    1 — добавить, 2 — показать, 3 — удалить, q — выход.
"""

import sys

import database
import utils

MENU = (
    "1. Добавить заметку\n"
    "2. Вывести все заметки\n"
    "3. Удалить заметку по номеру\n"
    "q. Выход\n"
)


def main():
    """Запустить интерактивное меню."""
    utils.clear_screen()
    print(f"Заметок в базе: {database.count()}\n")

    while True:
        print(MENU)
        choice = utils.get_input("Выберите действие: ").lower()

        if choice == "1":
            utils.add_note()
        elif choice == "2":
            utils.show_notes()
        elif choice == "3":
            utils.delete_note()
        elif choice in ("q", "quit", "exit", "0"):
            print("Пока!")
            break
        else:
            print(f"Неизвестное действие: {choice!r}. Введите 1, 2, 3 или q.")

        utils.pause()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nПрервано пользователем.")
        sys.exit(0)
