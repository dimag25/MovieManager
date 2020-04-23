# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app.py'],
             pathex=['C:\\Users\\dima\\PycharmProjects\\MovieDownloader'],
             binaries=[],
             datas=[('.\\eel_module\\', 'eel_module'), ('.\\Models\\', 'Models'), ('.\\api', 'api'), ('.\\DB', 'DB'), ('C:\\Users\\dima\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\eel', 'eel')],
             hiddenimports=['bottle_websocket'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='app',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
