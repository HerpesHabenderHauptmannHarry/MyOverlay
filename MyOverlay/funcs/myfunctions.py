from win32api import GetSystemMetrics
import pygame
import win32api
import win32con
import win32gui
import ctypes

OverlayRunning = 0
white = (255, 255, 255)
black = (0, 0, 0)
fuchsia = (255, 0, 128)
GWL_EXSTYLE = -20
WS_EX_APPWINDOW = 0x00040000
WS_EX_TOOLWINDOW = 0x00000080

_circle_cache = {}
def _circlepoints(r):
    r = int(round(r))
    if r in _circle_cache:
        return _circle_cache[r]
    x, y, e = r, 0, 1 - r
    _circle_cache[r] = points = []
    while x >= y:
        points.append((x, y))
        y += 1
        if e < 0:
            e += 2 * y - 1
        else:
            x -= 1
            e += 2 * (y - x) - 1
    points += [(y, x) for x, y in points if x > y]
    points += [(-x, y) for x, y in points if x]
    points += [(x, -y) for x, y in points if y]
    points.sort()
    return points


def render(text, font, opx=2):
    textsurface = font.render(text, True, white).convert_alpha()
    w = textsurface.get_width() + 2 * opx
    h = font.get_height()

    osurf = pygame.Surface((w, h + 2 * opx)).convert_alpha()
    osurf.fill((0, 0, 0, 0))

    surf = osurf.copy()

    osurf.blit(font.render(text, False, black).convert_alpha(), (0, 0))

    for dx, dy in _circlepoints(opx):
        surf.blit(osurf, (dx + opx, dy + opx))

    surf.blit(textsurface, (opx, opx))
    return surf


def StartOverlay():
    global OverlayRunning
    if not OverlayRunning:
        global text
        global textRect
        global screen
        OverlayRunning = 1
        screen_width = GetSystemMetrics(win32con.SM_CXSCREEN)
        screen_height = GetSystemMetrics(win32con.SM_CYSCREEN)
        pygame.init()
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)  # For borderless, use pygame.NOFRAME

        hwnd = pygame.display.get_wm_info()["window"]

        style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)

        style = style & ~WS_EX_APPWINDOW
        style = style | WS_EX_TOOLWINDOW
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, style)

        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                               win32gui.GetWindowLong(hwnd,
                                                      win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED | win32con.WS_EX_TOPMOST)
        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)
        
        screen.fill(fuchsia)
        pygame.display.update()

        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, screen_width, screen_height, 0)
        return 1
    else:
        return 0




def settext(text: str, PosX: int, PosY: int):
    global OverlayRunning
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            OverlayRunning = 0
    font = pygame.font.SysFont('Segoe UI Semibold', 30, False)
    screen.fill(fuchsia)  # Transparent background
    lines = str(text).splitlines()
    for i, l in enumerate(lines):
        screen.blit(render(l, font), (XPos // 2, PosY // 2 + 30 * i))
    pygame.display.update()
    
def KillOverlay():
    pygame.display.quit()
    OverlayRunning = 0
    
def StatusOverlay():
    return OverlayRunning
