import .buttons

def set_mouse(x, y):

def move_mouse(dx, dy):

def get_keysym(char):

def get_keycode(char):

def press(keycode):

def release(keycode):

def strike(keycode):

def type(string):
 for char in string:
  strike(get_keycode(char))

def click(button, down=None):
 if down == None:
  click(button, True)
  click(button, False)
  return
