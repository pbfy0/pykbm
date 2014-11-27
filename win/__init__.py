import sys, os.path
sys.path.append(os.path.dirname(__file__))
import ktypes
import constants
import ctypes as c
#print(constants.key)
m = constants.mouse
events = [[m.LEFTDOWN, m.MIDDLEDOWN, m.RIGHTDOWN],
		  [m.LEFTUP, m.MIDDLEUP, m.RIGHTUP]]
user32 = c.windll.user32
SI = user32.SendInput
SI.argtypes = [c.c_uint, ktypes.PINPUT, c.c_int]
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
getCursorPos = user32.GetCursorPos
getCursorPos.argtypes = [c.POINTER(ktypes.POINT)]

def send_input(inputs, n=1):
 SI(n, inputs, ktypes.ISIZE)
def _mouse_input(mi):
 it = ktypes.INPUTTYPE(mi=mi)
 inp = ktypes.INPUT(type=ktypes.INPUT_MOUSE, i=it)
 send_input(inp)

def set_mouse(x, y):
 (x, y) = (int(x/screensize[0]*65535), int(y/screensize[1]*65535))
 mi = ktypes.MOUSEINPUT(dx=x, dy=y, dwFlags=constants.mouse.ABSOLUTE | constants.mouse.MOVE)
 _mouse_input(mi)
def move_mouse(dx, dy):
 mi = ktypes.MOUSEINPUT(dx=round(dx), dy=round(dy), dwFlags=constants.mouse.MOVE)
 _mouse_input(mi)
def get_mouse():
 point = ktypes.POINT()
 getCursorPos(c.byref(point))
 return point.x, point.y

def _gen_key_inputs(st):
 o = []
 for i in st:
  ki = ktypes.KEYBOARDINPUT(wVk=0, wScan=ord(i), dwFlags=constants.key.UNICODE)
  it = ktypes.INPUTTYPE(ki=ki)
  o += [ktypes.INPUT(type=constants.input.KEYBOARD, i=it)]
  
  ki = ktypes.KEYBOARDINPUT(wVk=0, wScan=ord(i), dwFlags=constants.key.UNICODE | constants.key.KEYUP)
  it = ktypes.INPUTTYPE(ki=ki)
  o += [ktypes.INPUT(type=constants.input.KEYBOARD, i=it)]
 return o

def type(st):
 ins = _gen_key_inputs(st)
 l = len(ins)
 array_type = ktypes.INPUT * l
 array = array_type(*ins)
 send_input(array, l)

def click(button, down=None):
 if button > 3:
  raise NotImplementedError()
 if down == None:
  click(button, True)
  click(button, False)
  return
 e = events[0 if down else 1][button-1]
 mi = ktypes.MOUSEINPUT(dwFlags=e)
 it = ktypes.INPUTTYPE(mi=mi)
 inp = ktypes.INPUT(type=constants.input.MOUSE, i=it)
 send_input(inp)

def scroll(dy, dx=0):
	dx, dy = int(dx*120), int(dy*120)
	inps = []
	if(dy != 0):
		mi = ktypes.MOUSEINPUT(dwFlags=constants.mouse.WHEEL, mouseData=dy)
		it = ktypes.INPUTTYPE(mi=mi)
		inps += [ktypes.INPUT(type=constants.input.MOUSE, i=it)]
	if(dx != 0):
		mi = ktypes.MOUSEINPUT(dwFlags=constants.mouse.HWHEEL, mouseData=dx)
		it = ktypes.INPUTTYPE(mi=mi)
		inps += [ktypes.INPUT(type=constants.input.MOUSE, i=it)]
	l = len(inps)
	array_t = ktypes.INPUT * l
	array = array_t(*inps)
	send_input(array, l)