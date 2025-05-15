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

        try:
            with open(cls.FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                f.flush()  # ← 強制寫入到磁碟（防止打包時寫入不完整）
                os.fsync(f.fileno())  # ← 更強制確保寫入
            print(f"[儲存成功] {cls.FILE}")
        except Exception as e:
            print(f"[儲存失敗] {cls.FILE}：{e}")
            

    @classmethod
    def load(cls):
        if not os.path.exists(cls.FILE):
            return []
        with open(cls.FILE, "r", encoding="utf-8") as f:
            return json.load(f)

