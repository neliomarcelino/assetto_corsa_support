from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
build_options = {'packages': [], 'excludes': []}

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('main.py', base=base, target_name = 'rvz_support')
]

setup(name='rvz_support',
      version = '1.0',
      description = 'Support for RVZ Servers',
      options = {'build_exe': build_options},
      executables = executables)
