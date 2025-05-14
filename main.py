import tkinter as tk
from sticky_note import StickyNote  # 假設你把 StickyNote 寫在 sticky_note.py 裡
from NoteStorageManager import NoteStorageManager

class StickyNoteManager:
    def __init__(self):
        self.root = tk.Tk() #初始化，建立主視窗
        self.root.withdraw()  # 隱藏主視窗
        self.notes = [] #儲存顯示中的便利貼

        # 先建立一張貼紙（硬編碼）
        for data in NoteStorageManager.load():
            self.create_note(**data)

        if not self.notes:
            self.create_note()  # 至少保留一張


    def create_note(self, content="", x=100, y=100, width=200, height=150, font_size=12):
        note = StickyNote(
            master=self.root,
            manager=self,
            content=content,
            x=x,
            y=y,
            width=width,
            height=height,
            font_size=font_size
        )
        self.notes.append(note)

    def remove_note(self, note):    #移除便利貼
        if note in self.notes:
            self.notes.remove(note)
            note.destroy()
        if not self.notes:
            self.create_note()

    def close_all(self, quit_app=True):
        NoteStorageManager.save(self.notes)
        for note in self.notes:
            note.destroy()
        self.notes.clear()
        if quit_app:
            self.root.quit()


    def run(self):
        self.root.mainloop()

    def save_all_notes(self):
        NoteStorageManager.save(self.notes)


if __name__ == "__main__":
    manager = StickyNoteManager()
    manager.run()
