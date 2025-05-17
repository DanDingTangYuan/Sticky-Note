[中文版](./README.zh-TW.md)
# 📝 StickyNoteApp

A lightweight, multi-note desktop application built with Python's `tkinter`, designed for quick notes, reminders, and spontaneous ideas. Supports autosave and multiple sticky windows.

---

## 📦 Download & Run

> Visit the [Releases](https://github.com/DanDingTangYuan/Sticky-Note/releases) page to download the latest version.

### 🔧 Installation

1. Double-click `main.exe` to launch the application.  
2. A `data.json` file will be automatically created in the same folder upon first run.

⚠️ **If Windows Defender shows a warning on first launch, please allow it manually or add it to the trusted list.**

---

## ✨ Features

- 🗂 Multiple sticky note windows (each is an independent window)
- 🖱 Drag notes with the mouse
- 🔲 Resizable from the bottom-right corner
- 📐 Automatically adjusts window height based on content
- ✂️ Prevents excessive shrinking (keeps content visible)
- 🖋 Adjustable font size (`Ctrl + +` / `Ctrl + -`)
- ♻️ Autosave on window focus out
- 💾 Persistent data saved to `data.json`
- 📑 Right-click context menu:
  - Create a new sticky note
  - Close current note
  - Close all notes (keep app running)
  - Save and exit the app
  - Manual save option

---

## 🧠 Keyboard Shortcuts

| Shortcut            | Action              |
|---------------------|---------------------|
| `Ctrl + +`          | Increase font size  |
| `Ctrl + -`          | Decrease font size  |
| `Ctrl + Z / Y`      | Undo / Redo         |
| Right-click on note | Open context menu   |

---

## 🧪 Technical Info

- Python version: 3.11+
- GUI Framework: `tkinter`
- Packaged with: `PyInstaller`
- Automatically resolves data path in packaged `.exe` to ensure `data.json` is always saved in the same directory

---

## 👤 Author

Author: TangYuan  
If you have suggestions or bugs to report, please use the [GitHub Issues](https://github.com/DanDingTangYuan/Sticky-Note/issues) page 🙌

---

## 📜 License

This project uses a custom license:

- 📂 Free to use, modify, and learn from  
- ❌ **Commercial use is strictly prohibited**  
  (includes selling, app store publishing, paid licensing, corporate use, etc.)
- 📄 For full terms, see the [`LICENSE`](./LICENSE) file  
> For commercial use inquiries, please contact the author for written permission.
