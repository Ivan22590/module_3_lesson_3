"""utils.py — функции взаимодействия с пользователем.

Здесь всё, что связано с терминалом: очистка экрана, вывод списка, чтение
ввода и сценарии добавления/удаления заметок. Сама логика хранения живёт в
database.py.
"""

import os

import database


def clear_screen():
    """Очистить экран терминала (Windows / Linux / macOS)."""
    os.system("cls" if os.name == "nt" else "clear")


def get_input(prompt):
    """Считать строку и вернуть её без пробелов по краям."""
    return input(prompt).strip()


def pause():
    """Дождаться нажатия Enter, очистить экран и напечатать меню заново."""
    input("Нажмите Enter, чтобы продолжить...")
    clear_screen()


def show_notes():
    """Вывести все заметки на экран с номерами."""
    notes = database.get_all()

    if not notes:
        print("Заметок пока нет.")
        return

    print(f"\nВаши заметки ({len(notes)}):")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")
    print()


def add_note():
    """Спросить текст у пользователя и сохранить заметку."""
    text = get_input("Введите текст заметки: ")

    if not database.add(text):
        print("Пустая заметка не добавлена.")
        return

    print(f"Заметка добавлена. Всего заметок: {database.count()}")


def delete_note():
    """Спросить номер и удалить заметку."""
    notes = database.get_all()

    if not notes:
        print("Заметок пока нет — удалять нечего.")
        return

    show_notes()
    raw = get_input("Введите номер заметки для удаления: ")

    try:
        number = int(raw)
    except ValueError:
        print(f"Нужно было ввести число, а получено: {raw!r}.")
        return

    removed = database.delete(number)

    if removed is None:
        print(f"Заметки с номером {number} нет. Допустимые номера: 1-{len(notes)}.")
        return

    print(f"Удалена заметка {number}: {removed}")
