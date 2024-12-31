import win32gui

def enumHandler(hwnd, lParam):
    if win32gui.IsWindowVisible(hwnd):
        print(win32gui.GetWindowText(hwnd))
        if 'PooPz' in win32gui.GetWindowText(hwnd):
            win32gui.MoveWindow(hwnd, 0, 0, 760, 500, True)
            ...

win32gui.EnumWindows(enumHandler, None)
