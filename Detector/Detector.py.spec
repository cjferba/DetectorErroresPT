# -*- mode: python -*-
a = Analysis([os.path.join(HOMEPATH,'support\\_mountzlib.py'), os.path.join(HOMEPATH,'support\\useUnicode.py'), 'Detector.py.py'],
             pathex=['C:\\Users\\Carlosbasso\\Desktop\\pyinstaller-1.5.1'])
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=1,
          name=os.path.join('build\\pyi.win32\\Detector.py', 'Detector.py.exe'),
          debug=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT( exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name=os.path.join('dist', 'Detector.py'))
