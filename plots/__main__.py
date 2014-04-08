import os
import shutil

if __name__ == '__main__':
    if os.path.isdir('build'): shutil.rmtree('build')
    if not os.path.isdir('build'): os.makedirs('build')
