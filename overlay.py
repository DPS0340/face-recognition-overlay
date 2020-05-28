import tkinter
import win32api
import win32con
import pywintypes
from main import get_faces
from time import sleep
from win32api import GetSystemMetrics
import ctypes

# 이 파일을 실행하세요

# hidpi 관련 설정
ctypes.windll.shcore.SetProcessDpiAwareness(2)
root = tkinter.Tk()
root.lift()
root.attributes("-fullscreen", True)
root.wm_attributes("-topmost", True)
root.wm_attributes("-disabled", True)
root.wm_attributes("-transparentcolor", "black")
root.overrideredirect(True)
dpi = ctypes.windll.user32.GetDpiForWindow(root.winfo_id())
print(dpi)
_width = GetSystemMetrics(0)
_height = GetSystemMetrics(1)
w = tkinter.Canvas(root, width=_width, height=_height)
w.config(bg='black')
w.pack()


hWindow = pywintypes.HANDLE(int(root.frame(), 16))
# http://msdn.microsoft.com/en-us/library/windows/desktop/ff700543(v=vs.85).aspx
# The WS_EX_TRANSPARENT flag makes events (like mouse clicks) fall through the window.

# WS_EX_COMPOSITED 붙이면 프로그램이 동작하지 않음
# exStyle = win32con.WS_EX_COMPOSITED | win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
exStyle = win32con.WS_EX_LAYERED | win32con.WS_EX_NOACTIVATE | win32con.WS_EX_TOPMOST | win32con.WS_EX_TRANSPARENT
win32api.SetWindowLong(hWindow, win32con.GWL_EXSTYLE, exStyle)


def refresh():
    w.delete('all')
    print("refreshing...")
    face_locations, face_names = get_faces()
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        w.create_line(left, bottom, right, bottom, fill='green', width=2)
        w.create_line(left, top, right, top, fill='green', width=2)
        w.create_line(left, bottom, left, top, fill='green', width=2)
        w.create_line(right, bottom, right, top, fill='green', width=2)
        w.create_text((left + right) / 2 + 5, bottom +
                      10, text=name, fill='green', font=("맑은 고딕", 18))

        w.update()

    root.after(150, refresh)


# refresh 할당
root.after(150, refresh)
root.mainloop()
