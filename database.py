"""database.py — хранение заметок.

Единственный модуль, который знает, где и в каком формате лежат данные.
Заметки сохраняются в JSON-файл notes.json рядом с этим модулем, поэтому не
пропадают после закрытия программы.
"""

import json
from pathlib import Path

DB_FILE = Path(__file__).with_name("notes.json")


def save(notes):
    """Записать список заметок в JSON-файл."""
    DB_FILE.write_text(
        json.dumps(notes, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


def load():
    """Прочитать список заметок из JSON-файла.

    Если файла ещё нет или он повреждён, возвращается пустой список —
    программа при этом не падает.
    """
    if not DB_FILE.exists():
        return []

    try:
        data = json.loads(DB_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"Файл {DB_FILE.name} повреждён, начинаю с пустого списка.")
        return []

    return data if isinstance(data, list) else []


def add(text):
    """Добавить заметку и сохранить список на диск.

    Пустые заметки не добавляются. Возвращает True, если заметка добавлена.
    """
    text = text.strip()
    if not text:
        return False

    notes = load()
    notes.append(text)
    save(notes)
    return True


def get_all():
    """Вернуть все заметки в порядке добавления."""
    return load()


def delete(number):
    """Удалить заметку по её номеру (нумерация с 1).

    Возвращает текст удалённой заметки или None, если номера недопустим.
    """
    notes = load()

    if not isinstance(number, int) or not 1 <= number <= len(notes):
        return None

    removed = notes.pop(number - 1)
    save(notes)
    return removed


def count():
    """Вернуть количество заметок."""
    return len(load())
