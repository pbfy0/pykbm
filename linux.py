import Xlib.XK, Xlib.display, Xlib.X
from Xlib.ext import xtest
import buttons

display = Xlib.display.Display()
root = display.screen().root
SHIFT = 50

special_X_keysyms = {
    ' ' : "space",
    '\t' : "Tab",
    '\n' : "Return",  # for some reason this needs to be cr, not lf
    '\r' : "Return",
    '\b' : "BackSpace",
    '\e' : "Escape",
    '!' : "exclam",
    '#' : "numbersign",
    '%' : "percent",
    '$' : "dollar",
    '&' : "ampersand",
    '"' : "quotedbl",
    '\'' : "apostrophe",
    '(' : "parenleft",
    ')' : "parenright",
    '*' : "asterisk",
    '=' : "equal",
    '+' : "plus",
    ',' : "comma",
    '-' : "minus",
    '.' : "period",
    '/' : "slash",
    ':' : "colon",
    ';' : "semicolon",
    '<' : "less",
    '>' : "greater",
    '?' : "question",
    '@' : "at",
    '[' : "bracketleft",
    ']' : "bracketright",
    '\\' : "backslash",
    '^' : "asciicircum",
    '_' : "underscore",
    '`' : "grave",
    '{' : "braceleft",
    '|' : "bar",
    '}' : "braceright",
    '~' : "asciitilde"
    }

def set_mouse(x, y):
 root.warp_pointer(x, y)
 display.sync()

def get_mouse():
 pos = root.query_pointer()._data
 return pos['root_x'], pos['root_y']

def move_mouse(dx, dy):
 cx, cy = get_mouse
 set_mouse(cx + dx, cy + dy)

def _shifted(char):
 return char.isupper() or  char in '~!@#$%^&*()_+{}|:">?';

def _get_keysym(char):
 return Xlib.XK.string_to_keysym(char) or Xlib.XK.string_to_keysym(special_X_keysyms[char])

def _get_keycode(char):
 return display.keysym_to_keycode(_get_keysym(char))

def _press(keycode, down=None):
 if down == None:
  _press(keycode, True)
  _press(keycode, False)
  return
 xtest.fake_input(display, Xlib.X.KeyPress if down else Xlib.X.KeyRelease, keycode)
 display.sync()

def type(string):
 for char in string:
  shift = _shifted(char)
  if shift: _press(SHIFT)
  _press(_get_keycode(char))
  if shift: _release(SHIFT)

def click(button, down=None):
 if down == None:
  click(button, True)
  click(button, False)
  return
 xtest.fake_input(display, Xlib.X.ButtonPress if down else Xlib.X.ButtonRelease, button)
 display.sync()

def scroll(dy, dx=0):
 if dy != 0:
  button = buttons.SCROLLUP if dy > 0 else buttons.SCROLLDOWN
  for i in range(int(abs(dy))):
   click(button)
 if dx != 0:
  button = buttons.SCROLLRIGHT if dx > 0 else buttons.SCROLLLEFT
  for i in range(int(abs(dx))):
   click(button)