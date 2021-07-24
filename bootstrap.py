import os

from shutil import rmtree
from platform import system
from argparse import ArgumentParser

def make_clean():
    cwd = os.path.dirname(__file__)
    dirnames = ['__pycache__', 'build', 'dist']
    for d in dirnames:
        dirpath = os.path.join(cwd, d)
        if os.path.isdir(dirpath):
            rmtree(dirpath)

def make_executable():
    make_clean()
    os.system('pyinstaller main.spec')

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument(
        '--mode', type=str, default='install',
        choices=['clean', 'install'],
        help='This is a script which makes your life a lot easier :)'
    )
    args = parser.parse_args()
    mode = args.mode
    mode_func = {
        'clean': make_clean,
        'install': make_executable,
    }.get(mode)
    mode_func()
