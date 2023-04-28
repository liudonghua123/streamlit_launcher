# -*- mode: python ; coding: utf-8 -*-

import sys, os
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))   # Not works due to NameError: name '__file__' is not defined
sys.path.append(os.getcwd())
from utils import build_package_datas_item

datas = [
    build_package_datas_item("altair", "vegalite/v4/schema/vega-lite-schema.json", dir_mode=False),
    build_package_datas_item("streamlit", "static"),
    build_package_datas_item("streamlit", "runtime"),
    # ("./.streamlit", "./.streamlit"),
]

print(f'pyinstaller package using datas: {datas}')

block_cipher = None

a = Analysis(
    ['streamlit_launcher.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='streamlit_launcher',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='streamlit_launcher',
)
