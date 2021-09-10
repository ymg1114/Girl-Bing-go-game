# -*- mode: python ; coding: utf-8 -*-

import os
import sys

from platform import system

cwd = os.getcwd()

girl_imgs = os.path.join(cwd, 'image', 'girl', '*')
nice_imgs = os.path.join(cwd, 'image', 'nice', '*')

site_package_paths = [path for path in sys.path if path.endswith('site-packages')]
if not site_package_paths:
    raise ValueError('There is no valid path for site-packages!')

block_cipher = None
a = Analysis(
    ['ymg_pyside_mini_project1.py'],
    pathex=site_package_paths,
    binaries=[],
    # Put data(i.e. assets) under virtual 'image/'
    datas=[
        ('image', 'image'),
    ],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False
)
pyz = PYZ(
    a.pure, a.zipped_data, cipher=block_cipher
)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Girl bing-go',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    icon='winter.ico',
)