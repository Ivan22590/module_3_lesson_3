#!/usr/bin/env python3
"""Консольные заметки: добавление, просмотр и удаление заметок по номеру."""

import os
import sys

notes = []


def clear_screen():
    """Очистить экран терминала."""
    os.system("cls" if os.name == "nt" else "clear")


def add_note():
    """Считать строку текста и добавить её в список заметок."""
    text = input("Введите текст заметки: ").strip()
    if not text:
        print("Пустая заметка не добавлена.")
        return
    notes.append(text)
    print(f"Заметка добавлена. Всего заметок: {len(notes)}")


def show_notes():
    """Вывести все заметки на экран с номерами."""
    if not notes:
        print("Заметок пока нет.")
        return
    print(f"\nВаши заметки ({len(notes)}):")
    for index, note in enumerate(notes, start=1):
        print(f"{index}. {note}")
    print()


def delete_note():
    """Удалить заметку по её номеру."""
    if not notes:
        print("Заметок пока нет — удалять нечего.")
        return

    show_notes()
    raw = input("Введите номер заметки для удаления: ").strip()
    try:
        number = int(raw)
    except ValueError:
        print(f"Нужно было ввести число, а получено: {raw!r}.")
        return

    if not 1 <= number <= len(notes):
        print(f"Заметки с номером {number} нет. Допустимые номера: 1-{len(notes)}.")
        return

    removed = notes.pop(number - 1)
    print(f"Удалена заметка {number}: {removed}")


def main():
    """Запустить интерактивное меню."""
    menu = (
        "1. Добавить заметку\n"
        "2. Вывести все заметки\n"
        "3. Удалить заметку по номеру\n"
        "q. Выход\n"
    )

    while True:
        print(menu)
        choice = input("Выберите действие: ").strip().lower()

        if choice == "1":
            add_note()
        elif choice == "2":
            show_notes()
        elif choice == "3":
            delete_note()
        elif choice in ("q", "quit", "exit", "0"):
            print("Пока!")
            break
        else:
            print(f"Неизвестное действие: {choice!r}. Введите 1, 2, 3 или q.")

        input("Нажмите Enter, чтобы продолжить...")
        clear_screen()


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nПрервано пользователем.")
        sys.exit(0)
