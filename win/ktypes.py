import ctypes as c
import ctypes.wintypes as w

HCURSOR = c.c_int

class POINT(c.Structure):
 _fields_ = [('x', c.c_ulong),
             ('y', c.c_ulong)]

class MOUSEINPUT(c.Structure):
 _fields_ = [('dx', c.c_long),
             ('dy', c.c_long),
			 ('mouseData', w.DWORD),
			 ('dwFlags', w.DWORD),
			 ('time', w.DWORD),
			 ('dwExtraInfo', c.POINTER(c.c_ulong))]

class KEYBOARDINPUT(c.Structure):
 _fields_= [('wVk', w.WORD),
			('wScan', w.WORD),
			('dwFlags', w.DWORD),
			('time', w.DWORD),
			('dwExtraInfo', c.POINTER(c.c_ulong))]

class HARDWAREINPUT(c.Structure):
 _fields_ = [('uMsg', w.DWORD),
			 ('wParamL', w.WORD),
			 ('wParamH', w.WORD)]

class INPUTTYPE(c.Union):
 _fields_ = [('mi', MOUSEINPUT),
			 ('ki', KEYBOARDINPUT),
			 ('hi', HARDWAREINPUT)]

class INPUT(c.Structure):
 _anonymous_ = ('i',)
 _fields_ = [('type', w.DWORD),
			 ('i', INPUTTYPE)]

INPUT_MOUSE = 0
INPUT_KEYBOARD = 1
INPUT_HARDWARE = 2
ISIZE = c.sizeof(INPUT)
PINPUT = c.POINTER(INPUT)

XBUTTON1 = 0x1
XBUTTON2 = 0x2

# MOUSEEVENTF_ABSOLUTE = 0x8000
# MOUSEEVENTF_HWHEEL = 0x1000
# MOUSEEVENTF_MOVE = 0x1
# MOUSEEVENTF_MOVE_NOCOALESCE = 0x2000
# MOUSEEVENTF_LEFTDOWN = 0x2
# MOUSEEVENTF_LEFTUP = 0x4
# MOUSEEVENTF_RIGHTDOWN = 0x8
# MOUSEEVENTF_RIGHTUP = 0x10
# MOUSEEVENTF_MIDDLEDOWN = 0x20
# MOUSEEVENTF_MIDDLEUP = 0x40
# MOUSEEVENTF_VIRTUALDESK = 0x4000
# MOUSEEVENTF_WHEEL = 0x800
# MOUSEEVENTF_XDOWN = 0x80
# MOUSEEVENTF_XUP = 0x100

# KEYEVENTF_EXTENDEDKEY = 0x1
# KEYEVENTF_KEYUP = 0x2
# KEYEVENTF_SCANCODE = 0x8
# KEYEVENTF_UNICODE = 0x4