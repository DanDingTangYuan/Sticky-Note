import json
import os
import sys

def get_base_dir():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))

class NoteStorageManager:
    FILE = os.path.join(get_base_dir(), "data.json")

    @classmethod
    def save(cls, notes):
        data = [note.get_data() for note in notes]
        with open(cls.FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    @classmethod
    def load(cls):
        if not os.path.exists(cls.FILE):
            return []
        with open(cls.FILE, "r", encoding="utf-8") as f:
            return json.load(f)
