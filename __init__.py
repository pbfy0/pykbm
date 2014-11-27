import sys, os.path
sys.path.append(os.path.dirname(__file__))

import buttons

if sys.platform == 'linux2':
 from .linux import *

elif sys.platform == 'win32':
 from .win import *
