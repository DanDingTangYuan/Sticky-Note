import tkinter as tk
import tkinter.font as tkFont
from resizeable import ResizableMixin


class StickyNote(tk.Toplevel, ResizableMixin):
    def __init__(self, master=None, manager=None, content="", x=100, y=100, width=200, height=150, font_size=12):
        super().__init__(master)
        self.manager = manager
        self.geometry(f"{width}x{height}+{x}+{y}")
        self.configure(bg="lightyellow")
        self.overrideredirect(True)
        self.attributes('-topmost', True)
        self.font_size = font_size
        self.font = tkFont.Font(family="Arial", size=self.font_size)


        self.text = tk.Text(self, bg="lightyellow", wrap="word", bd=0,
                    font=("Arial", self.font_size),
                    undo=True, maxundo=-1)
        self.text.insert("1.0", content)
        self.text.pack(expand=True, fill="both")

        self.text.bind("<Button-1>", self.start_move)
        self.text.bind("<B1-Motion>", self.do_move)
        self.text.bind("<ButtonRelease-1>", self.end_move)
        self.text.bind("<Button-3>", self.menu)
        self.protocol("WM_DELETE_WINDOW", self.on_close)
        self.text.bind("<Control-plus>", lambda e: self.increase_font())
        self.text.bind("<Control-minus>", lambda e: self.decrease_font())
        self.text.bind("<Control-KP_Add>", lambda e: self.increase_font())
        self.text.bind("<Control-KP_Subtract>", lambda e: self.decrease_font())
        self.text.bind("<KeyRelease>", self.auto_resize_height)


        
        self.bind("<FocusOut>", self.on_focus_out)

        

        self.make_resizable()

    def start_move(self, event):
        self._x = event.x
        self._y = event.y

    def do_move(self, event):
        self.text.config(cursor="fleur")
        x = self.winfo_pointerx() - self._x
        y = self.winfo_pointery() - self._y
        self.geometry(f"+{x}+{y}")

    def end_move(self, event):
        self.text.config(cursor="")

    def reset_notes(self):
        self.manager.close_all(quit_app=False)
        self.manager.create_note()

    def menu(self, event):
        menu = tk.Menu(self, tearoff=0)
        menu.add_command(label="新增便利貼", command = self.manager.create_note)
        menu.add_command(label="刪除當前的便利貼", command = self.on_close)
        menu.add_command(label="刪除全部便利貼", command = self.reset_notes)
        menu.add_command(label="手動儲存", command=self.manager.save_all_notes)
        menu.add_command(label="儲存並關閉",command=lambda: self.manager.close_all(quit_app=True))
        menu.post(event.x_root, event.y_root)

    def on_close(self):
        if self.manager:
            self.manager.remove_note(self)
        else:
            self.destroy()
    
    def get_data(self):
        return {
            "content": self.text.get("1.0", "end-1c"),
            "x": self.winfo_x(),
            "y": self.winfo_y(),
            "width": self.winfo_width(),
            "height": self.winfo_height(),
            "font_size": self.font_size
        }

    def on_focus_out(self, event):
        self.manager.save_all_notes()

    def save_all_notes(self):
        from NoteStorageManager import NoteStorageManager
        NoteStorageManager.save(self.notes)

    def increase_font(self):
        self.font_size += 2
        self.text.config(font=("Arial", self.font_size))
        self.manager.save_all_notes()

    def decrease_font(self):
        self.font_size = max(6, self.font_size - 2)
        self.text.config(font=("Arial", self.font_size))
        self.manager.save_all_notes()

    def auto_resize_height(self, event=None):
        # 計算目前文字總行數
        line_count = int(self.text.index("end-1c").split(".")[0])

        # 每行大概佔 20 像素（這要根據你字體大小去估）
        line_height = int(self.font_size * 1.6)

        new_height = max(50, line_count * line_height)

        width = self.winfo_width()
        x = self.winfo_x()
        y = self.winfo_y()

        self.geometry(f"{width}x{new_height}+{x}+{y}")

        self.manager.save_all_notes()  # 自動儲存更新後的尺寸