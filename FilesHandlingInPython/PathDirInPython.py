import os
import pathlib


ROOT_DIR = os.path.abspath(os.curdir)
#print(ROOT_DIR)


rOOT_DIR = os.path.dirname(os.path.abspath("Screenshots"))
#print(rOOT_DIR)

ROOT_DIR1 = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
#print(ROOT_DIR1)
CONFIG_PATH = os.path.join(ROOT_DIR1, 'configuration.conf')  # requires `import os`
#print(CONFIG_PATH)


fn = os.path.join(os.path.abspath(os.pardir), 'Screenshots')
print(fn)# this will give u a project directory


PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
define = os.path.join(PROJECT_ROOT, 'Screenshots')
#print(define)
