import tkinter as tk

class ResizableMixin:
    def make_resizable(self):
        self._resizing = None

        grip = tk.Frame(self, cursor="bottom_right_corner", bg="#000000", width=5, height=5)
        grip.place(relx=1, rely=1, anchor="se")
        grip.bind("<Button-1>", lambda e: self.start_resize(e, "se"))
        grip.bind("<B1-Motion>", self.do_resize)

    def start_resize(self, event, direction):
        self._resizing = (direction, event.x_root, event.y_root, self.winfo_x(), self.winfo_y(), self.winfo_width(), self.winfo_height())

    def do_resize(self, event):
        direction, x0, y0, win_x, win_y, win_w, win_h = self._resizing
        dx = event.x_root - x0
        dy = event.y_root - y0

        x, y, w, h = win_x, win_y, win_w, win_h

        # 取得目前內容的行數與最長行的寬度
        lines = self.text.get("1.0", "end-1c").split("\n")
        max_line_width = max(self.font.measure(line) for line in lines)
        min_width = max(100, max_line_width + 20)  # 避免行被折

        line_count = int(self.text.index("end-1c").split(".")[0])
        line_height = int(self.font_size * 1.6)
        min_height = max(50, line_count * line_height)

        if 'e' in direction:
            w = max(min_width, win_w + dx)
        if 's' in direction:
            h = max(min_height, win_h + dy)
        if 'w' in direction:
            x = win_x + dx
            w = max(min_width, win_w - dx)
        if 'n' in direction:
            y = win_y + dy
            h = max(min_height, win_h - dy)

        self.geometry(f"{int(w)}x{int(h)}+{int(x)}+{int(y)}")
        self.manager.save_all_notes()
