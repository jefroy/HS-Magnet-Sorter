'''
installs packages depending on if inside a virtual environment or not
by following a file hierarchy thingy
'''

from os import system
import sys

folderName = 'reqs/'

def is_venv():
    return (hasattr(sys, 'real_prefix') or
            (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix))

if is_venv(): # detect venv and install these reqs
    print('Virtual Environment detected! Installing dev-reqs and reqs..')
    system('pip install -r' + folderName + 'dev-reqs.txt')
    system('pip install -r' + folderName + 'reqs.txt')
else:
    print("No Virtual Environment detected! Installing pre-reqs..")
    system('pip install -r' + folderName + 'pre-reqs.txt')